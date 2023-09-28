import os
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_year_from_url(url: str) -> str:
    # Get years 19XX or 20XX
    # Use the last year found in each URL. The first is the upload date.
    year = "0000"
    re_year = re.findall("((19|20)\d{2})", url)
    if re_year:
        year = re_year[-1][0]
    return year


def get_filename_from_url(url: str) -> str:
    filename = url.rsplit('/', 1)[-1]
    return filename


def get_nrmp_sms_pdf_urls() -> pd.DataFrame:
    # Get HTML page
    URL = "https://www.nrmp.org/match-data-analytics/archives/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get contents for specialties
    target = soup.find('h2', text="Specialties Matching Service")
    contents = []
    for sib in target.find_next_siblings():
        if sib.name == "h2":
            break
        else:
            print(sib.contents)
            if sib.contents:
                contents.append(sib.contents)

    # We only care about results and data (hardcoding it)
    contents_sms_rad_list = contents[1]
    contents_sms_rad = ''
    # Concatenating list to string
    for content in contents_sms_rad_list:
        if isinstance(content, str):
            contents_sms_rad += content
        else:
            contents_sms_rad += str(content)

    # Parse contents for links
    soup_sms = BeautifulSoup(contents_sms_rad, features="lxml")
    pdf_urls = []
    for link in soup_sms.findAll("a"):
        pdf_url = link.get("href")
        pdf_urls.append(pdf_url)
        print(f"Got URL: {pdf_url}")

    # Create DF and extract year
    df_pdf = pd.DataFrame(pdf_urls, columns=['url'])
    df_pdf['year'] = df_pdf['url'].apply(get_year_from_url)
    df_pdf['filename'] = df_pdf['url'].apply(get_filename_from_url)

    return df_pdf

def get_nrmp_archive_pdfs():
    df_pdf = get_nrmp_sms_pdf_urls()

    # Download PDFs
    home_dir = os.path.expanduser('~')
    dl_dir = os.path.join(home_dir, "Downloads", "nrmp_archives")
    if not os.path.exists(dl_dir):
        os.makedirs(dl_dir)
    for _, row_pdf in df_pdf.iterrows():
        local_filepath = os.path.join(dl_dir, row_pdf['filename'])
        if os.path.exists(local_filepath):
            print(f"File already exists (not downloading): {local_filepath}")
            continue
        response = requests.get(row_pdf['url'])
        if response.ok:
            with open(local_filepath, mode="wb") as file:
                file.write(response.content)
                print(f"Downloaded file: {row_pdf['filename']} "
                      f"to {local_filepath}")

    # Write out index
    index_filename = "nrmp_archive_index.csv"
    index_filepath = os.path.join(dl_dir, index_filename)
    df_pdf.to_csv(index_filepath, index=False)
    pass


if __name__ == '__main__':
    get_nrmp_archive_pdfs()
