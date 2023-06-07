from enum import Enum


class OrderType(str, Enum):
    ASC = 'ASC'
    DESC = 'DESC'
    NONE = 'NONE'
