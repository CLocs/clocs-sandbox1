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


def prepend_question_to_answer(col_map: Dict) -> Dict:
    new_map = {}
    # Get the questions
    q_only = {c: m for c, m in col_map.items() if re.match("^Q\d+$", c) or re.match("^Q\d+\_\d+$", c) or re.match("Q\d+\.\d+$", c)}
    # Prepend the questions to the answers
    for q_num, q_def in q_only.items():
        answers_exist = False
        for col, answer in col_map.items():
            # Find respective answers
            if (q_num + "_") in col and not q_num == col and q_def:
                a_num_re = re.search("A\d+$", col)
                if a_num_re:
                    answers_exist = True
                    a_num = a_num_re.group()
                    new_name = q_num + "_" + q_def + "-" + a_num + "_" + answer
                    new_map[col] = new_name
        if not answers_exist:
            new_name = q_num + "_" + q_def
            new_map[q_num] = new_name
    return new_map


def run_map_cols_from_sheet(main_filepath: str,
                            map_filepath: str,
                            map_file_sheet:str) -> None:
    # Load main file
    df_main = pd.read_excel(main_filepath, engine='openpyxl')

    # Load and parse mapping to dict
    col_map = load_col_map_from_file(map_filepath, map_file_sheet)
    col_map_exp = prepend_question_to_answer(col_map)

    # Apply mapping
    df_map = df_main.rename(col_map_exp, axis='columns')

    # Dump
    dump_exp_file(df_map, main_filepath, op_name='map')


if __name__ == '__main__':
    main_file = 'G:/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/v3 output/Revised Cancer_WISH_WB_exp.xlsx'
    map_file = 'G:/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/v3 output/Revised Cancer_WISH_WB_v3_legend.xlsx'
    map_file_sheet = 'Legend'
    run_map_cols_from_sheet(main_file, map_file, map_file_sheet)
