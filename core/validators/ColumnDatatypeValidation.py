from pandas import DataFrame

import pandas.api.types as ptypes
from core.common.Column import Column
from core.common.Exceptions import DatatypeMismatchException
from core.validators.BaseValidator import BaseValidator


class ColumnDatatypeValidation(BaseValidator):
    def validate(self, df: DataFrame) -> bool:
        try:
            if ptypes.is_numeric_dtype(df[Column.NAV.value]):
                return True
            else:
                raise DatatypeMismatchException("NAV is non numeric")
        except DatatypeMismatchException:
            return False  # TODO log csv file info
