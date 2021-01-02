from __future__ import unicode_literals
from distutils.core import setup
import py2exe, sys, os
from pathlib import Path
import youtube_dl
import eyed3

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    # windows = [{'script': "youtubeAudioConverter.py"}],
    console = ["youtubeAudioConverter.py"], #for stdin, replacing windows with console for input
    zipfile = None,
)