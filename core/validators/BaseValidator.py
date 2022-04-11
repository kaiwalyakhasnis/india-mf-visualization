from abc import abstractmethod
from pandas import DataFrame


class BaseValidator(object):
    @abstractmethod
    def validate(self, df: DataFrame) -> bool:
        pass
