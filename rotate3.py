# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
# getting subclip as video is large
# adding margin to the video
clip1 = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4").subclip(0, 5).margin(10)


# getting clip2 by mirroring over x axis
clip2 = clip1.fx(vfx.mirror_x)

# getting clip3 by mirroring over y axis
clip3 = clip1.fx(vfx.mirror_y)

# getting clip 4 by resising the clip
clip4 = clip1.resize(0.60)

# clips list
clips = [[clip1, clip2],
		[clip3, clip4]]


# stacking clips
final = clips_array(clips)

# showing final clip
final.ipython_display(width = 480)
