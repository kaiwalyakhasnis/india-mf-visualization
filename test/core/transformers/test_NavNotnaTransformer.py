from unittest import TestCase
import numpy as np
from pandas import DataFrame
import pandas as pd

from core.common.Column import Column
from core.transformers.NavNotnaTransformer import NavNotnaTransformer


def create_test_dataframe() -> DataFrame:
    test_data = {
        Column.SCHEME_CODE.value: [100612, 100613],
        Column.SCHEME_NAME.value: ["Sundaram Growth Fund-Dividend 1", "Sundaram Growth Fund-Dividend 2"],
        Column.ISIN_PAYOUT.value: ["INF903J01330", "INF903J01331"],
        Column.ISIN_DIV_REINVEST.value: ["INF903J01348", "INF903J01348"],
        Column.NAV.value: [100.00, np.nan],
        Column.REPURCHASE_PRICE.value: [100.0, np.nan],
        Column.SALE_PRICE.value: [3000.0, 6000.0],
        Column.DATE.value: ["01-Apr-2006", "01-Apr-2006"]
    }
    return pd.DataFrame(data=test_data)


class TestNavNotnaTransformer(TestCase):
    def test_transform(self):
        # arrange
        test_pd = create_test_dataframe()

        # act
        transformed_pd = NavNotnaTransformer().transform(test_pd)

        # assert
        self.assertTrue(transformed_pd.equals(
            pd.DataFrame(data={
                Column.SCHEME_CODE.value: [100612],
                Column.SCHEME_NAME.value: ["Sundaram Growth Fund-Dividend 1"],
                Column.ISIN_PAYOUT.value: ["INF903J01330"],
                Column.ISIN_DIV_REINVEST.value: ["INF903J01348"],
                Column.NAV.value: [100.00],
                Column.REPURCHASE_PRICE.value: [100.0],
                Column.SALE_PRICE.value: [3000.0],
                Column.DATE.value: ["01-Apr-2006"]
            })
        ))
