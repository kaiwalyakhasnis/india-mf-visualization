from pandas import DataFrame

from core.common.Column import Column


class NavNotnaTransformer(BaseException):
    def transform(self: DataFrame) -> DataFrame:
        return self[self[Column.NAV.value].notna()]
