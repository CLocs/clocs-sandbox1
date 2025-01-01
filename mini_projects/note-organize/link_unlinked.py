import fileinput
import os
import re
import tempfile
import shutil

debug_str_len_ext_post = 13
debug_str_len_ext_pre = 4

def link_unlinked(note_name: str, 
                  note_path: str, 
                  obsidian_vault_path: str):
    # Check obsidian vault path
    if not os.path.exists(obsidian_vault_path):
        print(f"Obsidian vault path does not exist: {obsidian_vault_path}")
        return
    
    # Check if note exists in obsidian vault
    note_path = os.path.join(obsidian_vault_path, note_path)
    if not os.path.exists(note_path):
        print(f"Note does not exist in obsidian vault: {note_path}")
        return
    
    # Make replace string
    note_replace_string = f"[[{note_name}]]"
    
    # Search all notes for references to note_name
    ref_dict = []
    all_files = []
    n_links = 0
    for root, dirs, files in os.walk(obsidian_vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if not os.path.exists(file_path):
                    continue
                all_files.append(file_path)
                with open(file_path, "r", encoding='utf-8') as f:
                    for i_line, line in enumerate(f):
                        (replaceable_link, i_start_outs, n_links) = valid_replace(line, note_name, note_replace_string, n_links)
                        if replaceable_link:
                            for i_start_out in i_start_outs:
                                ref_dict.append(
                                    {
                                        "path": file_path, 
                                        "i_line": i_line,
                                        "i_start": i_start_out
                                    }
                                )
    
    # Print
    print(f"Found {len(ref_dict)} references to {note_name} after searching {len(all_files)} files")
    # for i, ref in enumerate(ref_path):
    #     print(f"({i+1}/{len(ref_path)}) Found reference to {note_name} in {ref['path']} at line {ref['line']}")
    
    # Update references to note_name to note_obisidian_url
    for i, ref in enumerate(ref_dict):
        replaced = replace_str_in_file_line(ref["path"], ref["i_line"], ref["i_start"], note_name, note_replace_string)
        if replaced:
            # Update to replace a substring at i_start
            print(f"({i+1}/{len(ref_dict)}) Updated reference to {note_name} in {ref['path']}")
            billy = 1
    return True


def get_substring_with_buffer(line, i_start, orig_str) -> str:
    line_buff = len(line) - (i_start + len(orig_str))
    if line_buff > debug_str_len_ext_post:
        line_ext_end = debug_str_len_ext_post
    else:
        line_ext_end = line_buff
    # It's a legit replacement!
    line_buff_start = i_start - debug_str_len_ext_pre
    # if line_buff_start == 0:
    #     line_ext_start = 0
    if line_buff_start < 0:
        line_ext_start = debug_str_len_ext_pre + line_buff_start
    else:
        line_ext_start = debug_str_len_ext_pre
    substr_w_buffer = (f"{line[i_start+1:i_start+len(orig_str)+1] } << {line[i_start-line_ext_start:i_start+len(orig_str)+line_ext_end]}")
    return substr_w_buffer


def valid_replace(line, orig_str, replace_str, n_links):
    # Coarse check
    if orig_str in line and replace_str not in line:
        # Fine check
        # Require preceding whitespace
        reg_ex = r"\s" + orig_str
        line2 = line.replace("\n", "")
        match = re.finditer(reg_ex, line2)
        i_starts = [m.start() for m in match]
        if len(i_starts) == 0:
            return False, 0, n_links
        i_start_out = []
        for i_ref, i_start in enumerate(i_starts):
            # For some crazy reason, i_start is one behind of the actual start, so we must add +1 to i_start
            # Want to avoid replacing [[orig_str]]
            if line2[i_start-1:i_start+1] == "[[":
                continue
            # Want to avoid replacing [orig_str](link)
            elif line2[i_start-1] == "[":
                continue
            # Want to avoid ending in .md
            elif line2[i_start+len(orig_str)+1:i_start+len(orig_str)+4] == ".md":
                continue
            else:
                substr_w_buffer = get_substring_with_buffer(line2, i_start, orig_str)
                print(f"({n_links}): {substr_w_buffer}")
                n_links += 1
                i_start_out.append(i_start)
                return True, i_start_out, n_links
        return False, 0, n_links
    return False, 0, n_links


def replace_str_in_file_line(file_path, i_line, i_start, orig_str, replace_str):
    # Source: https://stackoverflow.com/a/39110/2643436

    if not os.path.exists(file_path):
        return False
    
    # Create temp file
    replaced = False
    n_links = 0
    fh, abs_path = tempfile.mkstemp()
    with os.fdopen(fh, 'w', encoding='utf-8') as new_file:
        with open(file_path, 'r', encoding='utf-8') as old_file:
            for i_l, line in enumerate(old_file):
                if i_l == i_line:
                    substr_w_buffer = get_substring_with_buffer(line, i_start, orig_str)
                    n_links += 1
                    print(f"({n_links}): Replacing: {orig_str} with {replace_str} in {substr_w_buffer}; file: {file_path}, line: {i_line}")
                    line = substring_replacer(line, orig_str, replace_str, i_start)
                    replaced = True
                new_file.write(line)
    # Copy the file permissions from the old file to the new file
    shutil.copymode(file_path, abs_path)
    # Remove original file
    os.remove(file_path)
    # Move new file
    shutil.move(abs_path, file_path)

    return replaced


def substring_replacer(line, orig_str, replace_str, i_insert):
    # raise an error if index is outside of the string
    if i_insert not in range(len(line)):
        return replace_str

    # if not erroring, but the index is still not in the correct range..
    if i_insert < 0:  # add it to the beginning
        return replace_str + line
    if i_insert >= len(line):  # add it to the end
        return line + replace_str

    # insert substring between "slice" of the original
    return line[:i_insert + 1] + replace_str + line[i_insert + len(orig_str) + 1:]


if __name__ == '__main__':
    note_name = "Addy"
    note_obisidian_url = "obsidian://open?vault=obsidian&file=People%2FAddy"
    obsidian_vault_path = "D:/My Drive/Resources/obsidian/"
    # obsidian_vault_path = "C:/Users/dasco/work_temp/obsidian_test"
    
    obsidian_vault_path_clean = os.path.normpath(obsidian_vault_path)

    note_url_clean = note_obisidian_url.replace("%2F", "/")
    note_path_local = note_url_clean.replace("obsidian://open?vault=obsidian&file=", "")
    note_absolute_path = os.path.join(obsidian_vault_path_clean, note_path_local)
    note_absolute_path = note_absolute_path + ".md"


    link_unlinked(note_name, note_absolute_path, obsidian_vault_path_clean)
