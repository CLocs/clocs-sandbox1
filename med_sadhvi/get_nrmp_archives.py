from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os


def get_year_from_url(url: str) -> str:
    # Get years 19XX or 20XX
    # Use the last year found in each URL. The first is the upload date.
    year = "0000"
    re_year = re.findall("((19|20)\d{2})", url)
    if re_year:
        year = re_year[-1][0]
    return year


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
    return df_pdf

def get_nrmp_archive_pdfs():
    df_pdf = get_nrmp_sms_pdf_urls()

    # Download PDFs
    os.path.expanduser('~')
    for _, row_pdf in df_pdf.iterrows():
        yeong = 1



    billy = 1
    pass


if __name__ == '__main__':
    get_nrmp_archive_pdfs()
