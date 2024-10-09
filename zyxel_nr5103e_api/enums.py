from enum import Enum


class Languages(Enum):
    """
    Router language.
    """
    en = "English"
    it = "Italian"
    cz = "Czech"
    nl = "Dutch"
    pt = "Portuguese"
    ru = "Russian"
    tr = "Turkish"


class SmsState(Enum):
    """
    SMS message state.
    """
    Unread = 0
    Read = 1
    Outgoing = 2
