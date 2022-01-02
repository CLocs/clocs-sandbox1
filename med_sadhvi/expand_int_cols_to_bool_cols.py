import pandas as pd
import os
from typing import List, Union


def compare_to_int(col_val: Union[float, int], ideal_value: int) -> int:
    billy = 1
    return int(col_val == ideal_value)


def run_expand_int_cols_to_bool_cols(filepath: str, col_list: List[str]) -> None:
    # Load file
    df = pd.read_excel(filepath, engine='openpyxl')
    df = df.dropna()

    # Create expanded columns
    for col in col_list:
        df[col] = df[col].astype(int)
        unique_vals = df[df[col].notna()][col].unique()
        for u_val in unique_vals:
            new_col_name = col + '_A' + str(u_val)
            df[new_col_name] = df[col].apply(compare_to_int, args=(u_val,))

    # Re-order Columns alpha-numerically
    cols = list(df.columns)
    cols_sorted = sorted(cols)
    df = df[cols_sorted]

    # TODO: move exceptional columns to front

    # Dump file
    dirpath, filename = os.path.split(filepath)
    basename,ext = os.path.splitext(filename)
    out_filename = basename + '_exp' + ext
    out_filepath = os.path.join(dirpath, out_filename)
    df.to_excel(out_filepath, index=False)
    print('Bam, done: int columns expanded to bool cols: ', out_filepath)


if __name__ == '__main__':
    filepath = 'E:/Google Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/Revised Cancer_WISH_WB_test.xlsx'
    col_names_to_expand = ['Q1']
    run_expand_int_cols_to_bool_cols(filepath, col_names_to_expand)
