from unittest import TestCase

import numpy as np
import pandas as pd

from core.common.Column import Column
from core.validators.ColumnNameValidation import ColumnNameValidation


class TestColumnValidation(TestCase):

    def test_validate_valid_column_names(self):
        # arrange
        test_pd = pd.DataFrame(data={
            Column.SCHEME_CODE.value: [100612, 100613],
            Column.SCHEME_NAME.value: ["Sundaram Growth Fund-Dividend 1", "Sundaram Growth Fund-Dividend 2"],
            Column.ISIN_PAYOUT.value: ["INF903J01330", "INF903J01331"],
            Column.ISIN_DIV_REINVEST.value: ["INF903J01348", "INF903J01348"],
            Column.NAV.value: [100.00, np.nan],
            Column.REPURCHASE_PRICE.value: [100.0, np.nan],
            Column.SALE_PRICE.value: [3000.0, 6000.0],
            Column.DATE.value: ["01-Apr-2006", "01-Apr-2006"]
        })

        # act and assert
        self.assertTrue(ColumnNameValidation().validate(test_pd))

    def test_validate_invalid_column_names(self):
        # arrange
        test_pd = pd.DataFrame(data={
            Column.SCHEME_CODE.value: [100612, 100613],
            "random": ["Sundaram Growth Fund-Dividend 1", "Sundaram Growth Fund-Dividend 2"],
            Column.ISIN_PAYOUT.value: ["INF903J01330", "INF903J01331"],
            Column.ISIN_DIV_REINVEST.value: ["INF903J01348", "INF903J01348"],
            Column.NAV.value: [100.00, np.nan],
            Column.REPURCHASE_PRICE.value: [100.0, np.nan],
            Column.SALE_PRICE.value: [3000.0, 6000.0],
            Column.DATE.value: ["01-Apr-2006", "01-Apr-2006"]
        })

        # act and assert
        self.assertFalse(ColumnNameValidation().validate(test_pd))
