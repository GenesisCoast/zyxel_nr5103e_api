from dataclasses import dataclass

from marshmallow_dataclass import dataclass, fields
from marshmallow import Schema


@dataclass
class DataAccessLayer:
    """
    Data access layer (DAL) response.
    """
    result = fields.String(required=True)
    ReplyMsg = fields.String(required=True)
    ReplyMsgMultiLang = fields.String(required=False)
    Object = fields.List(fields.Nested(fields.Dict), required=False)
    sessionKey = fields.String(required=False)
    Schema = Schema


class RouterResponse[T]:
    """
    Response from the ZyXEL NR5103E router.
    """
    dal: DataAccessLayer
    object: T

    def __init__(self, response: dict):
        dal = DataAccessLayer.Schema.load(response)

        self.dal = dal
        self.object = dal.Object