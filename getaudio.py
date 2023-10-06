
# Import everything needed to edit video clips
from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
  
# getting only first 3 seconds
clip = clip.subclip(0, 5)
  
# getting audio from the clip
audioclip = clip.audio
  
# printing audio clip
print(audioclip)

audioclip.write_audiofile("test.mp3")