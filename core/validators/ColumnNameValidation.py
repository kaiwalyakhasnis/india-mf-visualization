from pandas import DataFrame

from core.common.Column import Column
from core.validators.BaseValidator import BaseValidator


class ColumnNameValidation(BaseValidator):
    def validate(self, df: DataFrame) -> bool:
        return all(Column.has_value(column) for column in df.columns)
