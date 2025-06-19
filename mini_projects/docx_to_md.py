import os
import pypandoc
import shutil
import mammoth
from convert_docx_to_html import convert


def convert_docx_to_md(dir_path: str, out_path: str) -> None:
    # # Copy
    # shutil.copytree(dir_path, out_path)
    # print(f"Copied all files from {dir_path} to {out_path}")

    # Convert
    for root, dir_names, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith("docx"):
                # Get rel path
                rel_path = root.replace(dir_path, "")
                rel_path = rel_path.replace("//", "")
                rel_path = rel_path.replace("\\", "")
                out_dir_path = os.path.normpath(os.path.join(out_path, rel_path))
                in_file_path = os.path.normpath(os.path.join(root, filename))
                in_filename, _ = os.path.splitext(filename)
                # out_filename = in_filename + ".md"
                out_filename = in_filename + ".html"
                out_file_path = os.path.join(out_dir_path, out_filename)
                os.makedirs(out_dir_path, exist_ok=True)
                # output = pypandoc.convert_file(in_file_path, "md", outputfile=out_file_path)

                html = convert(root, filename)
                with open(out_file_path, "w") as markdown_file:
                    markdown_file.write(html)

                # # Works, but images are shit
                # with open(in_file_path, "rb") as docx_file:
                #     result = mammoth.convert_to_html(docx_file)
                # with open(out_file_path, "w") as markdown_file:
                #     markdown_file.write(result.value)

                print(f"Converted and wrote file: {out_file_path}")
                # os.remove(in_file_path)
                # print(f"Removed original file: {in_file_path}")
    pass


if __name__ == '__main__':
    dir_path = "C:/Users/dasco/OneDrive/Documents/test_onenote/Test Notebook"
    out_path = "C:/Users/dasco/OneDrive/Documents/test_onenote/test"
    convert_docx_to_md(dir_path, out_path)
