import base64
from typing import List
import requests

from smspdudecoder.codecs import GSM

from zyxel_nr5103e_api.models import DataAccessLayer, RouterResponse
from zyxel_nr5103e_api.models.basic_information import BasicInformation
from zyxel_nr5103e_api.models.sim import Sim
from zyxel_nr5103e_api.models.sms import Sms, SmsState


class ZyxelNr5103eClient:
    """
    Client for the ZyXEL NR5103E router API.
    """

    __success_code = 'ZCFG_SUCCESS'

    def __init__(self, host: str, username: str, password: str):
        """
        Constructor for the ZyXEL NR5103E client.
        """
        self.host = host
        self.username = username
        self.__base64_password = base64.b64encode(password)

    def __enter__(self):
        """
        Context manager entry for the ZyXEL NR5103E client.
        """
        self.session = requests.Session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit for the ZyXEL NR5103E client.
        """
        self.host = None
        self.username = None
        self.password = None
        self.base64_password = None
        self.session.__exit__(exc_type, exc_val, exc_tb)
        self.session = None

    def __checkLogin(self):
        """
        Check if the user is logged in.

        Raises:
            Exception: If the user is not logged in.
        """
        if not self.logged_in:
            raise Exception("User is not logged in, please call the login method first.")

    def __get_dal(self, oid: str) -> DataAccessLayer:
        """
        Send a DAL request.

        Parameters:
            oid: The name of the data to get from the Data Access Layer.

        Returns:
            The response from the Data Access Layer.
        """
        self.__checkLogin()

        response = self.session.post(
            url=f"https://{self.host}/cgi-bin/DAL?oid={oid}",
            headers=self.__get_headers()
        )

        self.__is_success(response)
        return response.json()

    def __get_headers(self) -> dict:
        """
        Get the standard headers for a request.

        Returns:
            A dictionary with the standard headers.
        """
        return {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept: application/json, text/javascript, */*; q=0.01',
            'Accept-Language: en-GB,en;q=0.5',
            'Accept-Encoding: gzip, deflate, br, zstd',
            'Content-Type: application/x-www-form-urlencoded; charset=UTF-8',
            'If-Modified-Since: Thu, 01 Jun 1970 00:00:00 GMT',
            'X-Requested-With: XMLHttpRequest',
            f'Origin: https://{self.host}',
            'DNT: 1',
            'Connection: keep-alive',
            'Cookie: Session=hii9XRc3DCZHq9XbvBJQvMBowFoRjZnp; Session=qUQVsY2EnhCIiR3AJg6c7yIFdfDqV4qu',
            'Sec-Fetch-Dest: empty',
            'Sec-Fetch-Mode: cors',
            'Sec-Fetch-Site: same-origin',
            'Sec-GPC: 1'
        }
    
    def __is_success(self, response: requests.Response) -> bool:
        """
        Check if the response is successful.

        Parameters:
            response: The response to check.

        Returns:
            True if the response is successful, False otherwise.
        """
        return response.ok & response.result == self.__success_code
    
    def clear_sms(self) -> RouterResponse:
        """
        Deletes all SMS messages.
        """
        sms = self.get_sms()
        obj_indexes = [mes.ObjIndex for mes in sms.object.SMS_Inbox]

        return self.delete_sms(obj_indexes)
    
    def clear_incoming_sms(self) -> RouterResponse:
        """
        Deletes all the incoming SMS messages.
        """
        sms = self.get_sms()
        obj_indexes = [mes.ObjIndex for mes in sms.object.SMS_Inbox if mes.State != SmsState.Outgoing]

        return self.delete_sms(obj_indexes)
    
    def clear_outgoing_sms(self) -> RouterResponse:
        """
        Deletes all the outgoing SMS messages.
        """
        sms = self.get_sms()
        obj_indexes = [mes.ObjIndex for mes in sms.object.SMS_Inbox if mes.State == SmsState.Outgoing]

        return self.delete_sms(obj_indexes)

    def delete_sms(self, *obj_indexes: List[str]) -> RouterResponse[None]:
        """
        Deletes an SMS message.

        Parameters:
            obj_indexes: Index of the SMS message to delete.

        Returns:
            The deletion response from the Data Access Layer.
        """
        self.__checkLogin()

        response = self.session.delete(
            url=f"https://{self.host}/cgi-bin/DAL?oid=cellwan_sms&sessionkey={self.session_key}&objIndex={','.join(obj_indexes)}",
            headers=self.__get_headers()
        )

        self.__is_success(response)
        return RouterResponse[None](response.json())
    
    def get_basic_information(self) -> BasicInformation:
        """
        Gets the basic information about the router.

        Returns:
            A tuple with a root DataAccessLayerResponse and a dictionary with the basic information.
        """
        response = self.session.get(
            url=f"https://{self.host}/getBasicInformation",
            headers=self.__get_headers()
        )

        return BasicInformation.Schema.load(response.json())
    
    def get_sim(self) -> RouterResponse[Sim]:
        """
        Lists all SMS messages.

        Returns:
            A tuple with a root DataAccessLayerResponse and a list of SIM details.
        """
        return RouterResponse[Sim](self.__get_dal(oid='cellwan_sim'))
    
    def get_sms(self) -> RouterResponse[Sms]:
        """
        Gets the SMS details, including all the incoming and outgoing messages.

        Returns:
            A tuple with a root DataAccessLayerResponse and a list of SMS messages.
        """
        return RouterResponse[Sms](self.__get_dal(oid='cellwan_sim'))
    
    def login(self) -> bool:
        """
        Performs a user login.

        Returns:
            True if the login was successful, False otherwise.
        """
        response = self.session.post(
            url=f"https://{self.host}/UserLogin",
            data={
                'Input_Account': self.username,
                'Input_Passwd': self.__base64_password,
                'currLang': 'en',
                'RememberPassword': 0,
                'SHA512_password': False
            },
            headers=self.__get_headers()
        )

        self.logged_in = self.__is_success(response)
        self.session_key = response.json().get('sessionkey')
        
        return self.logged_in
    
    def send_gsm_sms(self, send_to: str, message: str) -> RouterResponse[None]:
        """
        Sends an SMS message.

        Parameters:
            send_to: The number to send the SMS to.
            message: The message to send.

        Returns:
            The response from the Data Access Layer.
        """
        self.__checkLogin()
        encoded_message = GSM.encode(message)

        response = self.session.post(
            url=f"https://{self.host}/cgi-bin/DAL?oid=cellwan_sms&timedelay=1&sessionkey={self.session_key}",
            headers=self.__get_headers(),
            data={
                'SMS_Format': 0,
                'SMS_CharacterSet': 'GSM',
                'SMS_To': send_to,
                'SMS_ContentLength': message.length,
                'SMS_TimeStamp': '',
                'SMS_Content': encoded_message,
                'SMS_Content_divLen': [message.length],
                'SMS_Content_divData': [encoded_message]
            }
        )

        self.__is_success(response)
        return RouterResponse[None](response.json())