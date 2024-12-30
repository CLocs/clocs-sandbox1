import os
import pandas as pd


def move_day_files():
    # Reformat file name to YYYY-MM-DD.md
    # Find source file names in day format: YYYY-MM-DD.txt


    # Move to new directory

    # Make target file path
    # Make new extension MD

    # If contains YYYY-MM-DD and not YYYY-MM-DD.md, then queue file to list for debug warning / log.

	# Add a "-" to the start of every line if not already
    pass


def format_day_filenames(top_dir_path: str, out_path: str):
    # Find source file names in day format: YYYY-MM-DD.txt
    
    # If contains YYYY-MM-DD and not YYYY-MM-DD.md, then queue file to list for debug warning / log.
    # Make target file path

    pass


def format_day_files(top_dir_path, out_path):
    # Add a "-" to the start of every line if not already
    pass


if __name__ == '__main__':
    top_dir_path = "D:/My Drive/Resources/Backups/life/life"
    out_path = "D:/My Drive/Resources/Backups/life/flat"
    format_day_filenames(top_dir_path, out_path)
    format_day_files(top_dir_path, out_path)
    move_day_files()
