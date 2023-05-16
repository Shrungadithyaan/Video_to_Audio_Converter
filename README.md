# Video to Audio Converter

This Python script demonstrates how to convert a video file to an audio file using the `moviepy` library. It utilizes the `os` and `sys` modules for file handling and the `VideoFileClip` class from `moviepy.editor` for video conversion.

## Installation

To run this script, you need to install the `moviepy` library. You can install it using the following command:

```
pip install moviepy
```

## Usage

```python
import os
import sys
from moviepy.editor import VideoFileClip

def convert(file, e="mp3"):
    fname, ext = os.path.splitext(file)
    VideoFileClip(file).audio.write_audiofile(f"{fname}.{e}")

convert("new.mp4")
print("done")
```

In this script, we define a function called `convert` that takes a video file as input and converts it to an audio file. The `fname` variable stores the base name of the input file, while the `ext` variable stores its extension. The `VideoFileClip` class is used to load the video file, and the `write_audiofile` method is used to write the audio portion of the video to a new file with the specified extension (`e`). By default, the output file will be saved with the same name as the input file, but with the specified extension.

To use this script, simply call the `convert` function with the path to your video file as the argument. You can also specify the desired audio file extension by passing it as the second argument (e.g., `convert("new.mp4", "wav")`).

After the conversion is complete, the script will print "done" to indicate that the process has finished.


## Acknowledgments

Special thanks to the creators of the `moviepy` library for providing a simple and powerful solution for video editing and conversion in Python.