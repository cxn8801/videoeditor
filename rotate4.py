
# Import everything needed to edit video clips
from moviepy.editor import *
 
# loading video dsa gfg intro video
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
 
# clipping of the video 
# getting video for only starting 10 seconds
clip = clip.subclip(19, 40)
 
# rotating video by 180 degree
clip = clip.rotate(180)
 
# Reduce the audio volume (volume x 0.5)
clip = clip.volumex(4)
 
# showing clip
clip.ipython_display(width = 280)

clip.write_videofile('result.mp4')