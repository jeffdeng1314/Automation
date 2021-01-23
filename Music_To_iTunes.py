import os
from pathlib import Path
from DL_Folder_Organizer import downloadFolderPath

def moveMusicToItunes():
    downloadPath = downloadFolderPath.downloadPath

    src = downloadPath + "\\Music"

    os.system(f'move {src}\\* \"D:\Music\Automatically Add to iTunes\"')


if __name__ == "__main__":
    moveMusicToItunes()