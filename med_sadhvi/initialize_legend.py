import docx
from typing import Dict
from collections import OrderedDict
import re


def get_Q_para_num(doc: docx.Document) -> Dict:
    qp_dict = OrderedDict()
    for ip, para in enumerate(doc.paragraphs):
        qnum = re.findall('Q(\d+)', para.text)
        # if para.text.startswith('Q')
        if qnum:
            if len(qnum) > 1:
                print(f'Found many Qs: {qnum}, skipping...')
                continue
            curr_question = qnum[0]
            qp_dict[curr_question] = {}
            qp_dict[curr_question]['para_num'] = ip
    return qp_dict


def find_next_para_nums(q_para_dict: Dict) -> Dict:
    for i in range(len(q_para_dict)):
        q, _ = list(q_para_dict.items())[i]
        if i < len(q_para_dict) - 1:
            q_para_dict[q]['para_num_next'] = list(q_para_dict.items())[i+1][1]['para_num']
        else:
            q_para_dict['para_num_next'] = float('nan')
    return q_para_dict


def paras_to_question_dict(doc: docx.Document) -> Dict:
    q_para_dict = get_Q_para_num(doc)
    para_dict = find_next_para_nums(q_para_dict)
    billy = 1
    pass


def run_parser(docx_filepath: str) -> None:
    legend_dict = {}
    doc = docx.Document(docx_filepath)
    para_dict = paras_to_question_dict(doc)
    pass


if __name__ == '__main__':
    docx_filepath = '/Volumes/Google Drive/My Drive/Projects/Med_Sadhvi/Female Sexual Dysfunction/WISH Survey (1).docx'
    run_parser(docx_filepath)
