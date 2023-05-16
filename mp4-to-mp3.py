import os, sys

from moviepy.editor import VideoFileClip

def convert(file, e="mp3"):
    fname , ext = os.path.splitext(file)
    VideoFileClip(file).audio.write_audiofile(f"{fname}.{e}")

convert("new.mp4")
print("done")