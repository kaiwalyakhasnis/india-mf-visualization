from functools import reduce
import os

import numpy as np
import pandas as pd
from core.transformers.NavNotnaTransformer import NavNotnaTransformer
from core.validators.ColumnDatatypeValidation import ColumnDatatypeValidation
from core.validators.ColumnNameValidation import ColumnNameValidation

validators = [
    ColumnNameValidation(),
    # ColumnDatatypeValidation()
]

transformers = [
    NavNotnaTransformer()
]

"""
Extract --> Transform --> Load 
"""


def perform_etl(files):
    report_df = pd.DataFrame(data={})

    for file in files:
        print(file)
        df = pd.read_csv(f"../data/{file}", sep=';')
        df = df.replace(to_replace='N.A', value=np.nan, regex=True)
        if all(validator.validate(df) for validator in validators):
            report_df = pd.concat(
                [report_df,
                 reduce(
                     lambda result, transformer: transformer.transform(result),  # function
                     transformers,  # sequence
                     df)]  # initial
            )
        else:
            print(f"{file} has issue")
    report_df.to_csv("../output/report.csv")


if __name__ == '__main__':
    perform_etl(os.listdir("../data"))
