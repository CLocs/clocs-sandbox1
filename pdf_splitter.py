import sys
import os
from PyPDF2 import PdfWriter, PdfReader

"""
Best practice
    1. Run splitter: python pdf_splitter.py [filepath] 1 10
    (Note: file size is often large, eg, 100s of MB)
    2. Open in Adobe Reader and Save As PDF
"""


def pdf_splitter(filepath, start, end):
    # we will save new splited pdf as "nameofpdf splitted.pdf"
    # example if pdf name is "abc.pdf" then it will be saved as "abc splitted.pdf"
    dir_path, filename = os.path.split(filepath)
    file_basename, file_ext = os.path.splitext(filename)
    new_filename = file_basename + "_split.pdf"
    new_filepath = os.path.join(dir_path, new_filename)

    read_file = PdfReader(open(filepath, "rb"))  # read pdf

    new_pdf = PdfWriter()  # create write object
    start -= 1
    try:
        with open(new_filepath, "wb") as f:
            for i in range(start, end):
                new_pdf.add_page(read_file.pages[i])
                new_pdf.write(f)
                i += 1
            print(f"PDF split successfully: {new_filepath}")
    except Exception as e:
        print(e)


# First step is to check all command line arguments
if len(sys.argv) < 4:
    # if arguments are less then 4 then we will show error message to users.
    print("*" * 50)
    print("Invalid Agruments")
    print("-" * 50)
    print("python pdfsplits.py pdf_file_name_with_full_path start_page_number end_page_number")
    print("-" * 50)
    print("Example")
    print("python pdfsplits.py 'c:\\\\Users\\\\a.pdf' 2 5")
    print("*" * 50)
else:
    file_path = sys.argv[1]  # file name of PDF file which user want to split
    start_page = int(sys.argv[2])  # start page number
    end_page = int(sys.argv[3])  # end page number
    pdf_splitter(file_path, start_page, end_page)
