import os
from pathlib import Path

# https://www.geeksforgeeks.org/junk-file-organizer-python/
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".csv", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "MUSIC": [".mp3"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 


def organizer():
    username = os.environ['USERNAME']

    downloadPath = f"C:\\Users\\{username}\\Downloads"

    for entry in os.scandir(downloadPath):
        if entry.is_dir():
            continue

        file_path = Path(entry).suffix.lower()
        # print(entry.path)

        if file_path in FILE_FORMATS:
            dir_path = Path(f"{downloadPath}\\{FILE_FORMATS[file_path]}")

            # FileExistsError exception will be ignored
            dir_path.mkdir(exist_ok=True)

            # use move instead of mv for cmd (windows)
            os.system(f'move \"{entry.path}\" {dir_path}')


def generate():
    username = os.environ['USERNAME']

    downloadPath = f"C:\\Users\\{username}\\Downloads"

    for i in range(20):
        f = "testing" + str(i)
        os.system(f'touch {downloadPath}\\{f}.txt')


if __name__ == "__main__":
    organizer()
    # generate()


