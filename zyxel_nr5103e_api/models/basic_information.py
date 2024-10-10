from enum import Enum

from dataclasses import dataclass

from marshmallow_dataclass import dataclass, fields
from marshmallow import Schema


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


@dataclass
class BasicInformation:
    """
    Basic information about the router.
    """
    result = fields.String(required=True)
    ModelName = fields.String(required=True)
    SoftwareVersion = fields.String(required=True)
    CurrentLanguage = fields.Enum(Languages)
    AvailableLanguages = fields.String(required=True)
    RememberPassword = fields.Boolean()
    RemoAddr_Type = fields.String(required=True)
    AppCustomization = fields.Int(required=True)
    Schema = Schema