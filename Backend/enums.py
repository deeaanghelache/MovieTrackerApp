from enum import Enum


class LinkType(Enum):
    ACCOUNT_CONFIRMATION = 'ACCOUNT_CONFIRMATION',
    PASSWORD_RESET = 'PASSWORD_RESET'
    OTHER = 'OTHER'
