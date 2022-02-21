import pandas as pd
import os
import re
from typing import Dict, List, Union
import numpy as np
from expand_int_cols_to_bool_cols import dump_exp_file

def clean_description(desc1: str) -> str:
    if type(desc1) in [float, int]:
        if np.isnan(desc1):
            desc2 = ''
        else:
            desc2 = str(desc1)
    else:
        desc2 = desc1
    # Remove =
    desc3 = desc2.replace('=', '')
    # Remove numbers
    desc4 = re.sub('\d', '', desc3)
    # Remove leading and trailing spaces
    desc5 = re.sub('\s*$', '', desc4)
    desc6 = re.sub('^\s*', '', desc5)
    # Remove *
    desc7 = re.sub('\*', '', desc6)
    # Replace space with underscore
    desc8 = re.sub('\s', '_', desc7)
    return desc8


def load_col_map_from_file(map_filepath, map_file_sheet) -> Dict:
    df_map = pd.read_excel(map_filepath, engine='openpyxl',
                           sheet_name=map_file_sheet)
    df_map = df_map.loc[:, ~df_map.columns.str.contains('^Unnamed')]
    df_map['map_name'] = df_map['Description'].apply(clean_description)
    # Convert to dictionary
    return df_map.set_index('Question').to_dict()['map_name']


def run_map_cols_from_sheet(main_filepath: str,
                            map_filepath: str,
                            map_file_sheet:str) -> None:
    # Load main file
    df_main = pd.read_excel(main_filepath, engine='openpyxl')

    # Load and parse mapping to dict
    col_map = load_col_map_from_file(map_filepath, map_file_sheet)

    # Apply mapping
    new_cols = []
    for col in df_main.columns:
        if col in col_map:
            new_cols.append("".join((col, ': ', col_map[col])))
        else:
            new_cols.append(col)

    df_main.columns = new_cols

    # Dump
    dump_exp_file(df_main, main_filepath, op_name='map')
    # df_main.to_csv('G:/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/testout.csv')

if __name__ == '__main__':
    main_file = '/Volumes/Google Drive/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/v1 output/Revised Cancer_WISH_WB_exp.xlsx'
    map_file = '/Volumes/Google Drive/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/v1 output/Revised Cancer_WISH_clean_exp3.xlsx'
    map_file_sheet = 'Legend'
    run_map_cols_from_sheet(main_file, map_file, map_file_sheet)
