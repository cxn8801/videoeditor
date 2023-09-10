import cv2
import sys
from moviepy.editor import VideoFileClip
import moviepy.editor as mpy
from moviepy.video.fx.all import crop

# Read video
video = cv2.VideoCapture("chaplin-modern-times-non-sense-song-720.mp4")

# Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read first frame.
ok, frame = video.read()
if not ok:
    print('Cannot read video file')
    sys.exit()
    
video.release()

# Define an initial bounding box if you know it
#    bbox = (488*2, 266*2, 629*2, 730*2)

# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI('Select Area', frame, False)
cv2.destroyAllWindows()

print(bbox)

clip = mpy.VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
(w, h) = clip.size

cropped_clip = crop(clip, x1=bbox[0], y1=bbox[1], width=bbox[2], height=bbox[3])
# cropped_clip = crop(clip, width=320, height=320, x_center=w/2, y_center=h/2)
cropped_clip.write_videofile('video.mp4')