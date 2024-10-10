from dataclasses import dataclass

from marshmallow_dataclass import dataclass, fields
from marshmallow import Schema


@dataclass
class Sim:
    """
    Details on the SIM card.
    """
    USIM_Status = fields.Str
    USIM_IMSI = fields.Str
    USIM_ICCID = fields.Str
    USIM_Auto_Unlock = fields.Bool
    USIM_PIN_Protection = fields.Bool
    USIM_PIN_STATE = fields.Str
    USIM_PIN_RemainingAttempts = fields.Int
    USIM_PUK_RemainingAttempts = fields.Int
    Schema = Schema