import fileinput
import os
import tempfile
import shutil


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
    for root, dirs, files in os.walk(obsidian_vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if not os.path.exists(file_path):
                    continue
                all_files.append(file_path)
                with open(file_path, "r", encoding='utf-8') as f:
                    for line in f:
                        if note_name in line and note_replace_string not in line:
                            ref_dict.append(
                                {
                                    "path": file_path, 
                                    "line": line
                                }
                            )
    
    # Print
    print(f"Found {len(ref_dict)} references to {note_name} after searching {len(all_files)} files")
    # for i, ref in enumerate(ref_path):
    #     print(f"({i+1}/{len(ref_path)}) Found reference to {note_name} in {ref['path']} at line {ref['line']}")
    
    # Update references to note_name to note_obisidian_url
    for i, ref in enumerate(ref_dict):
        replaced = replace(ref["path"], note_name, note_replace_string)
        if replaced:
            print(f"({i+1}/{len(ref_dict)}) Updated reference to {note_name} in {ref['path']}")
    pass


def replace(file_path, orig_str, replace_str):
    if not os.path.exists(file_path):
        return False
    
    # Create temp file
    replaced = False
    fh, abs_path = tempfile.mkstemp()
    with os.fdopen(fh, 'w', encoding='utf-8') as new_file:
        with open(file_path, 'r', encoding='utf-8') as old_file:
            for line in old_file:
                if orig_str in line and replace_str not in line:
                    replaced = True
                    line = line.replace(note_name, replace_str)
                new_file.write(line)
    # Copy the file permissions from the old file to the new file
    shutil.copymode(file_path, abs_path)
    # Remove original file
    os.remove(file_path)
    # Move new file
    shutil.move(abs_path, file_path)

    return replaced


if __name__ == '__main__':
    note_name = "Addy"
    note_obisidian_url = "obsidian://open?vault=obsidian&file=People%2FAddy"
    obsidian_vault_path = "D:/My Drive/Resources/obsidian/"
    obsidian_vault_path = "C:/Users/dasco/work_temp/obsidian_test"
    
    obsidian_vault_path_clean = os.path.normpath(obsidian_vault_path)

    note_url_clean = note_obisidian_url.replace("%2F", "/")
    note_path_local = note_url_clean.replace("obsidian://open?vault=obsidian&file=", "")
    note_absolute_path = os.path.join(obsidian_vault_path_clean, note_path_local)
    note_absolute_path = note_absolute_path + ".md"


    link_unlinked(note_name, note_absolute_path, obsidian_vault_path_clean)
