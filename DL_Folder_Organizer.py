import os
from pathlib import Path

# https://www.geeksforgeeks.org/junk-file-organizer-python/
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],

    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],

    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],

    "Documents": [".oxps", ".pages", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps",
                  ".rvg", ".rtf", ".rtfd", ".wpd"],

    "Microsoft Documents": [".xls", ".xlsx", ".ppt",
                  ".pptx", ".csv",".docx", ".doc", ".dotx", ".docm", ".dox" ],

    "Archives": [".a", ".ar", ".cpio", ".iso",
                 ".dmg", ".rar", ".xar"],
    
    "Zip Files": [".tar", ".gz", ".rz", ".7z",
                  ".zip"],

    "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma", ".flac"],

    "Music": [".mp3"],
    "MATLAB": [".m"],
    "Icons": [".ico"],
    "Plain Text": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 

class downloadFolderPath:

    username = os.environ['USERNAME']
    downloadPath = f"C:\\Users\\{username}\\Downloads"

    def __init__(self):
        pass

    


def organizer():

    for entry in os.scandir(downloadFolderPath.downloadPath):
        if entry.is_dir():
            continue

        file_path = Path(entry).suffix.lower()
        # print(entry.path)

        if file_path in FILE_FORMATS:
            # print(FILE_FORMATS[file_path])
            dir_path = Path(f"{downloadFolderPath.downloadPath}\\{FILE_FORMATS[file_path]}")

            # FileExistsError exception will be ignored
            dir_path.mkdir(exist_ok=True)

            # use move instead of mv for cmd (windows)
            os.system(f'move \"{entry.path}\" \"{dir_path}\"')


# def generate():

#     for i in range(20):
#         f = "testing" + str(i)
#         os.system(f'touch {downloadFolderPath.downloadPath}\\{f}.txt')


if __name__ == "__main__":
    organizer()
    # generate()


