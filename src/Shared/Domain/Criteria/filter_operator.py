from enum import Enum


class FilterOperator(str, Enum):
    EQUAL = '='
    NOT_EQUAL = '!='
    GT = '>'
    LT = '<'
    CONTAINS = 'CONTAINS'
    NOT_CONTAINS = 'NOT_CONTAINS'
