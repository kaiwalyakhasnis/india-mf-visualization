from abc import abstractmethod
from pandas import DataFrame


class BaseTransform(object):
    @abstractmethod
    def transform(self, df: DataFrame) -> DataFrame:
        pass
