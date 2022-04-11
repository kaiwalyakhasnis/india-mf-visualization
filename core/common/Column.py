from enum import Enum


class Column(Enum):
    SCHEME_CODE = "Scheme Code"
    SCHEME_NAME = "Scheme Name"
    ISIN_PAYOUT = "ISIN Div Payout/ISIN Growth"
    ISIN_DIV_REINVEST = "ISIN Div Reinvestment"
    NAV = "Net Asset Value"
    REPURCHASE_PRICE = "Repurchase Price"
    SALE_PRICE = "Sale Price"
    DATE = "Date"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
