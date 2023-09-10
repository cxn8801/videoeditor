# Import everything needed to edit video clips
from moviepy.editor import *
	
# loading video file clip
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
	
# clipping of the video
# getting video for only starting 10 seconds
clip = clip.subclip(0, 5)
	
# Reduce the audio volume (volume x 0.5)
clip = clip.volumex(0.5)
	
# Generate a text clip
txt_clip = TextClip("GfG-MoviePy", fontsize = 75, color = 'green')
	
# setting position of text in the center and duration will be 5 seconds
txt_clip = txt_clip.set_pos('bottom').set_duration(5)
	
# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])
	
# showing video
video.write_videofile("result.mp4")
