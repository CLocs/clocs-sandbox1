import os
import pandas as pd
import pdfquery
from py_pdf_parser.loaders import load_file


def get_nrmp_index(nrmp_files_dir: str) -> pd.DataFrame:
    index_filename = "nrmp_archive_index.csv"
    index_filepath = os.path.join(nrmp_files_dir, index_filename)
    df_nrmp = pd.read_csv(index_filepath)
    return df_nrmp


def run_nrmp_parser(nrmp_files_dir: str) -> None:
    df_nrmp = get_nrmp_index(nrmp_files_dir)

    for _, row_nrmp in df_nrmp.iterrows():
        local_filepath = os.path.join(nrmp_files_dir, row_nrmp['filename'])
        # pdf = pdfquery.PDFQuery(local_filepath)
        # pdf.load()
        pdf = load_file(local_filepath)
        # Both PDF loaders hang on these ~20 MB files :(
        yeong = 1
        continue

    pass


if __name__ == '__main__':
    home_dir = os.path.expanduser('~')
    dl_dir = os.path.join(home_dir, "Downloads", "nrmp_archives")
    if not os.path.exists(dl_dir):
        print("Can't find NRMP index. Run get_nrmp_archives.py")
        exit(0)

    run_nrmp_parser(dl_dir)
