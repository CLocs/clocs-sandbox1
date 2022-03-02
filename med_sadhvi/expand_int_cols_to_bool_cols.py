import pandas as pd
import os
from typing import List, Union
import numpy as np


def dump_exp_file(df: pd.DataFrame,
                  filepath: str,
                  op_name: str='') -> str:
    dirpath, filename = os.path.split(filepath)
    basename, ext = os.path.splitext(filename)
    out_filename = basename + '_' + op_name + ext
    out_filepath = os.path.join(dirpath, out_filename)
    df.to_excel(out_filepath, index=False)
    return out_filepath


def get_unique_ints_with_commas(col_vals: pd.Series) -> List:
    unique_vals = col_vals[col_vals.notna()].unique()
    unique_vals_out = unique_vals

    # Deal with commas: find them, split them, merge them
    non_comma_vals = [v for v in unique_vals if ',' not in str(v)]
    comma_vals = [v for v in unique_vals if ',' in str(v)]
    comma_val_splits = []
    for comma_val in comma_vals:
        comma_val_splits.extend(comma_val.split(','))
    if comma_val_splits:
        # Remove spaces
        comma_val_splits2 = [v.replace(' ', '') for v in comma_val_splits]
        # Turn to ints
        comma_val_splits3 = [int(v) for v in comma_val_splits2]
        # Merge with unique values
        all_vals = non_comma_vals + comma_val_splits3
        # Remove duplicates
        s_all = pd.Series(all_vals)  #, dtype=int)
        unique_vals_out = s_all.unique()
    # Sort unique values
    unique_vals_int = [int(v) for v in unique_vals_out]
    unique_vals_sort = sorted(unique_vals_int)
    return unique_vals_sort


def compare_to_int(col_val: Union[float, int], ideal_value: int) -> int:
    out_val = 0
    if type(col_val) == str or not np.isnan(col_val):
        out_val = str(ideal_value) in str(col_val)
    return int(out_val)


def is_bool_series(col_vals: List) -> bool:
    # Convert from string to int
    valid_types = [int, bool]
    if (len(col_vals) == 1 or len(col_vals) == 2) and \
            all([type(val) in valid_types for val in col_vals]):
        return True
    else:
        return False


def expand_columns(df: pd.DataFrame, cols_exp: List[str]) -> pd.DataFrame:
    cols_out = []
    cols12 = []
    col_one_value = {}
    for col in df.columns:
        if col in cols_exp:
            unique_vals = get_unique_ints_with_commas(df[col])
            # Boolean columns should be one column (not expanded)
            if is_bool_series(unique_vals):
                cols_out.append(col)
                # Special case: 1,2 -> 0,1
                if len(unique_vals) == 2 and all([v in [1, 2] for v in unique_vals]):
                    cols12.append(col)
                    df[col].replace(1, 0, inplace=True)
                    df[col].replace(2, 1, inplace=True)
                if len(unique_vals) == 1:
                    col_one_value[col] = unique_vals[0]
            else:
                # Add a new column for each value and check value equality
                for u_val in unique_vals:
                    new_col_name = col + '_A' + str(u_val)
                    df[new_col_name] = df[col].apply(compare_to_int, args=(u_val,))
                    cols_out.append(new_col_name)
        else:
            cols_out.append(col)
    # Re-order
    df = df[cols_out]
    # Warnings
    if cols12:
        print(f'Warning: cols {cols12} have values 1,2. Make sure they are not of values 1,2 of possible 0,1,2.')
    if col_one_value:
        for col1, value1 in col_one_value.items():
            print(f'Warning: col: value only had 1 value: {col1}:{value1}')
    return df


def check_exp_cols(df: pd.DataFrame, cols_exp_in: List) -> List:
    cols_exp_check = []
    for col in cols_exp_in:
        if col in df.columns:
            cols_exp_check.append(col)
        else:
            print(f'Warning: skipping {col} because not in file.')
    return cols_exp_check


def run_expand_int_cols_to_bool_cols(filepath: str, cols_exp: List[str]) -> None:
    # Load file
    df = pd.read_excel(filepath, engine='openpyxl')

    cols_exp = check_exp_cols(df, cols_exp)
    # TODO: sort cols_exp. Note: cols_exp.sort() does not work because Q7, Q70
    # Create expanded columns and track order
    df = expand_columns(df, cols_exp)

    # Dump file
    out_filepath = dump_exp_file(df, filepath, op_name='exp')
    print('Bam, done: int columns expanded to bool cols: ', out_filepath)


if __name__ == '__main__':
    # # Testing
    # filepath = 'E:/Google Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/Revised Cancer_WISH_WB_test.xlsx'
    # col_names_to_expand = ['Q1']

    # Inputs
    # filepath = 'E:/Google Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/Revised Cancer_WISH_WB.xlsx'
    filepath = 'G:/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/v3 output/Revised Cancer_WISH_WB.xlsx'

    col_names_to_expand = ['Q1', 'Q1A_OH', 'Q1A_PA', 'Q1A_MI', 'Q3', 'Q3A_F',
                           'Q3A_M', 'Q3A_NB', 'Q3A_GN', 'Q3A_GNC',
                           'Q3A_TGF', 'Q3A_TGM', 'Q3A_GQ', 'Q3A_NA', 'Q7',
                           'Q9', 'Q11', 'Q13', 'Q15', 'Q17',
                           'Q19', 'Q78', 'Q80', 'Q81', 'Q83', 'Q84',
                           'Q85', 'Q86', 'Q87', 'Q89', 'Q91', 'Q92',
                           'Q98', 'Q25_1', 'Q25_2', 'Q25_3', 'Q25_4', 'Q27',
                           'Q29', 'Q31', 'Q33_1', 'Q33_2', 'Q33_3',
                           'Q33_4', 'Q33_5', 'Q33_6', 'Q33_7', 'Q33_8',
                           'Q33_9', 'Q39', 'Q45', 'Q47', 'Q49', 'Q51',
                           'Q53', 'Q57', 'Q59', 'Q63', 'Q65', 'Q67', 'Q69',
                           'Q71', 'Q73', 'Q75', 'Q77', 'Q79', 'Q81',
                           'Q83', 'Q85', 'Q87','Q81.1', 'Q83.1', 'Q85.1',
                           'Q87.1', 'Q89.1', 'Q91.1', 'Q93.1', 'Q89', 'Q91',
                           'Q95', 'Q97', 'Q99', 'Q100_1', 'Q100_2', 'Q100_3',
                           'Q101', 'Q103', 'Q105',
                           'Q107', 'Q109', 'Q111', 'Q113', 'Q115', 'Q117',
                           'Q119', 'Q123_1', 'Q123_2', 'Q123_3',
                           'Q123_4', 'Q123_5', 'Q123_6', 'Q123_7', 'Q123_8',
                           'Q123_9', 'Q123_10', 'Q123_11',
                           'Q123_12', 'Q123_13', 'Q125', 'Q129', 'Q131',
                           'Q133', 'Q135', 'Q137', 'Q139', 'Q141_1',
                           'Q141_2', 'Q141_3', 'Q145_1', 'Q145_2', 'Q145_3',
                           'Q150', 'Q151']
    run_expand_int_cols_to_bool_cols(filepath, col_names_to_expand)
