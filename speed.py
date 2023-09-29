# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("input.mp4")

# getting subclip from it
clip = clip.subclip(0, 9)

# applying speed effect
final = clip.fx( vfx.speedx, 5)

# showing final clip
final.write_videofile('output.mp4')
