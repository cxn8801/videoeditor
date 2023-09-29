# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("BVR_2023_06_16_12_56_13.mp4")


# showing final clip
clip.write_videofile('output.mp4')
