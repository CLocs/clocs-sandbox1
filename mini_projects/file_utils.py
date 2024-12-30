import os


def remove_empty_directories(root_path) -> None:
    for root, dir_names, filenames in os.walk(root_path):
        if not len(os.listdir(root)):
            os.rmdir(root)
            print(f"Dir is empty, deleting: {root}")


if __name__ == '__main__':
    dir_path = "C:/Users/dasco/OneDrive/Documents/test_onenote/Colin's Notebook HTML"
    remove_empty_directories(dir_path)
