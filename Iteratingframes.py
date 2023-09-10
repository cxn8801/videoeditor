# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
	
# getting only first 5 seconds
clip = clip.subclip(0, 5)

# iterating frames
frames = clip.iter_frames()

# counter to count the frames
counter = 0

# using loop to transverse the frames
for value in frames:
	
	# incrementing the counter
	counter += 1
	
# printing the value of the counter
print("Counter Value ", end = " : ")
print(counter)

# showing clip
clip.ipython_display(width = 360)
