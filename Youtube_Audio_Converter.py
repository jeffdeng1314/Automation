from __future__ import unicode_literals
import youtube_dl
import os
from DL_Folder_Organizer import downloadFolderPath
import eyed3


# removing anything with [] () 
INDICATORS = {
            '[' : ']',
            '(' : ')',
            '【' : '】'
        }

AVOID_CHARACTERS = {
    # \ / : * ? " < > |
    # A file cannot contain these characters

    '\\' : '',
    '/' : '_',
    ':' : '',
    '*' : '',
    '?' : '',
    '"' : "'",
    '<' : '',
    '>' : '',
    '|' : '_'
}

# Downloads to the Download folder 
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
        
        urls = input(str('Enter YouTube URL: '))
        # urls = os.sys.argv[1]

        # Could be a playlist or just a single video
        playlist = ydl.extract_info(f'{urls}',download=True)

        for video in playlist['entries']:
            trackTitle = video['title']

            if not trackTitle.isascii():
                continue
            
            print("trackTitle: ", trackTitle)

            for c in trackTitle:
                if c in AVOID_CHARACTERS:
                    trackTitle = trackTitle.replace(c,AVOID_CHARACTERS[c])

            
            print('After replacement with _: ' + trackTitle)

            newTrackTitle = trackTitle    
            # looping through the trackk title to remove anything from INDICATORS
            # Assuming the title won't contain [()] or ([]) or any of these combinations 
            start = end = -1
            for i in range(len(trackTitle)):
                # Make sure we can detect an indicator first
                if start >= 0:
                    if trackTitle[i] == INDICATORS[trackTitle[start]]:
                        end = i

                        # remove the white space before [ or (, it's kinda a cheat way
                        print(f'Start: {start}, End: {end}')
                        newTrackTitle = trackTitle[:start-1] + trackTitle[end+1:]
                        break

                if trackTitle[i] in INDICATORS:
                    start = i
                    continue


            print('!!!newTrackTitle: ', newTrackTitle)
            print('**trackTtile: ',trackTitle)
            # To songs like artist - song title [lyrics]??
            if '-' in newTrackTitle:
                artist = newTrackTitle.split('-')[0]
                # [1:] to remove the single white space in the front
                title = newTrackTitle.split('-')[1][1:]

                # loadFile = savePath + "/" + trackTitle + ".mp3"
                loadFile = savePath + '/' + trackTitle + ".mp3"
                print("LoadFile: ",loadFile)
                e = eyed3.load(loadFile)
                e.tag.artist = artist
                e.tag.title = title
                e.rename(title)
                e.tag.save()




if __name__ == "__main__":
    youtubeAudioConverter()