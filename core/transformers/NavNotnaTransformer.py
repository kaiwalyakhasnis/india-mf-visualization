from pandas import DataFrame

from core.common.Column import Column
from core.transformers.BaseTransform import BaseTransform


class NavNotnaTransformer(BaseTransform):
    def transform(self, df: DataFrame) -> DataFrame:
        return df[df[Column.NAV.value].notna()]
