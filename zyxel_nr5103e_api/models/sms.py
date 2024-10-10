from enum import Enum

from dataclasses import dataclass
from typing import List

from marshmallow_dataclass import dataclass, fields
from marshmallow import Schema


class SmsState(Enum):
    """
    SMS message state.
    """
    Unread = 0
    Read = 1
    Outgoing = 2


@dataclass
class SmsMessage:
    """
    SMS message in the inbox.
    """
    ObjIndex: int = fields.Int
    MsgIndex: int = fields.Int
    MsgID: str = fields.Str
    State: str = fields.Enum(SmsState)
    FromType: int = fields.Int
    From: str = fields.Method(serialize="get_from", deserialize="set_from")
    TimeStamp: str = fields.Str
    CharacterSet: int = fields.Int
    Content: str = fields.Method(serialize="get_content", deserialize="set_content")
    Schema = Schema

    def get_content(self, obj):
        return obj.Content.encode("utf-8").hex()

    def set_content(self, obj):
        return bytes.fromhex(obj.Content).decode("utf-8")
    
    def get_from(self, obj):
        if any(c.isalpha() for c in obj.Content):
            return obj.From.encode("utf-8").hex()
        else:
            return obj.From

    def set_from(self, obj):
        if any(c.isalpha() for c in obj.Content):
            return bytes.fromhex(obj.From).decode("utf-8")
        else:
            return obj.From


@dataclass
class Sms:
    """
    The WAN SMS message details (overall configuration).
    """
    SMS_Enable: int = fields.Bool
    SMS_UsedSpace: int = fields.Int
    SMS_TotalSpace: int = fields.Int
    SMS_Inbox: List[SmsMessage] = fields.List(fields.Nested(SmsMessage))
    Schema = Schema