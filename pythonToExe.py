from distutils.core import setup
import py2exe, sys, os
from pathlib import Path

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "downloadOrganizer.py"}],
    zipfile = None,
)