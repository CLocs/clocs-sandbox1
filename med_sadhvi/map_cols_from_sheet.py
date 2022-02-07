import pandas as pd
import os
import re
from typing import Dict, List, Union
import numpy as np

def clean_description(description: str) -> str:
    if type(description) in [float, int]:
        if np.isnan(description):
            desc = ''
        else:
            desc = str(description)
    else:
        desc = description
    # Remove =
    desc2 = desc.replace('=', '')
    # Remove numbers

    # Remove leading and trailing spaces
    # Replace space with underscore
    # Remove *

    return ''


def load_col_map_from_file(map_filepath, map_file_sheet) -> Dict:
    df_map = pd.read_excel(map_filepath, engine='openpyxl',
                           sheet_name=map_file_sheet)
    df_map = df_map.loc[:, ~df_map.columns.str.contains('^Unnamed')]
    df_map['map_name'] = df_map['Description'].apply(clean_description)
    # Convert to dictionary
    billy = 1


def run_map_cols_from_sheet(main_filepath: str,
                            map_filepath: str,
                            map_file_sheet:str) -> None:
    # Load main file
    df_main = pd.read_excel(main_filepath, engine='openpyxl')
    col_map = load_col_map_from_file(map_filepath, map_file_sheet)

    # Parse mapping to dict
    # Apply mapping
    # Dump
    pass


if __name__ == '__main__':
    main_file = 'E:/Google Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/Revised Cancer_WISH_WB_exp.xlsx'
    map_file = 'E:/Google Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/Revised Cancer_WISH_clean_exp3.xlsx'
    map_file_sheet = 'Legend'
    run_map_cols_from_sheet(main_file, map_file, map_file_sheet)
