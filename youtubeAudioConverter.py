from __future__ import unicode_literals
import youtube_dl
import os
from downloadOrganizer import downloadFolderPath
import eyed3


# Same shit, don't need it
def youtubeAudioConverter():

    savePath = downloadFolderPath.downloadPath
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl' : savePath + '/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        d
        info_dict = ydl.extract_info('https://www.youtube.com/watch?v=ChcSCG9e2xE',download=True)
        audioTitle = info_dict.get("title", None)

        print(info_dict)
        artist = audioTitle.split('-')[0]
        title = audioTitle.split('-')[1]

        loadFile = savePath + "/" + audioTitle + ".mp3"
        e = eyed3.load(loadFile)
        e.tag.artist = artist
        e.tag.title = title
        e.rename(title)
        e.tag.save()




if __name__ == "__main__":
    youtubeAudioConverter()