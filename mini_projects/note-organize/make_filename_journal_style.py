import os
import re
import shutil
import tempfile


def make_filename_journal_style(input_dir_path, output_dir_path):
    for root, _, files in os.walk(input_dir_path):
        for file in files:
            if file.endswith(".txt"):
                input_file_path = os.path.join(root, file)
                # Check for date in filename: YYYY-MM-DD
                matches_date_dash = re.search(r"(\d{4}-\d{2}-\d{2})(.*).txt", file)
                matches_date_no_dash = re.search(r"(\d{8})(.*).txt", file)
                if matches_date_dash:
                    # Rename file: YYYY-MM-DD.md
                    output_filename = f"{matches_date_dash.group(1)}.md"
                    output_file_path = os.path.join(output_dir_path, output_filename)
                    # Check for text after date
                    text_after_date = matches_date_dash.group(2)
                # Check for date in filename: YYYYMMDD
                elif matches_date_no_dash:
                    # Rename file: YYYY-MM-DD.md
                    date_no_dash = matches_date_no_dash.group(0)
                    output_filename = f"{date_no_dash[:4]}-{date_no_dash[4:6]}-{date_no_dash[6:8]}.md"
                    output_file_path = os.path.join(output_dir_path, output_filename)
                    # Check for text after date
                    text_after_date = matches_date_no_dash.group(2)
                # Some other file name format -- copy it over as-is, renamed to MD
                else:
                    basename, _ = os.path.splitext(file)
                    output_filename = f"{basename}.md"
                    non_journal_out_path = os.path.join(output_dir_path, "non-journal")
                    output_file_path = os.path.join(non_journal_out_path, output_filename)
                    text_after_date = ""
                
                # copy file and rename. If there is text after the date, move it to the top of the file
                if text_after_date:
                    # Remove starting space or underscore
                    header_text = text_after_date.lstrip()
                    if header_text[0] == "_":
                        header_text = header_text[1:]
                    # Move text to header of file -- requires making a new/temp file
                    temp_file_path = insert_line_at_top(input_file_path, header_text)
                    shutil.copymode(input_file_path, temp_file_path)
                    shutil.move(temp_file_path, output_file_path)
                else:
                    output_file_dir_path = os.path.dirname(output_file_path)
                    os.makedirs(output_file_dir_path, exist_ok=True)
                    shutil.copy(input_file_path, output_file_path)
                print(f"Renamed file: {file} --> {output_filename}; Moved from {input_file_path} --> {output_file_path}")
    return


def insert_line_at_top(orig_file_path: str, new_line: str, header: int = 1):
    fh, new_abs_path = tempfile.mkstemp()
    with os.fdopen(fh, 'w', encoding='utf-8') as new_file:
        with open(orig_file_path, 'r', encoding='utf-8') as old_file:
            # Insert line at top
            new_line_header = "#" * header + " " + new_line + "\n"
            new_file.write(new_line_header)
            # Insert rest of file
            for line in old_file:
                new_file.write(line)
    return new_abs_path


if __name__ == "__main__":
    input_path = "D:\\My Drive\\Resources\\Backups\\life\\life"
    output_path = "D:\\My Drive\\Resources\\Backups\\life\\life_journal_style"
    make_filename_journal_style(input_path, output_path)
