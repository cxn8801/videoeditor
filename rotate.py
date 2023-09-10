# Import everything needed to edit video clips
from moviepy.editor import *
  
# loading video dsa gfg intro video and getting only first 5 seconds
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4").subclip(0, 5)
  
# setting margin
clip1 = clip.margin(40)
  
# rotating clip by 180 degree to get the clip3
clip2 = clip.rotate(180).set_start(4)
  
# creating a composite video
final = CompositeVideoClip([clip1, clip2])
  
# showing final clip
final.ipython_display(width = 480)