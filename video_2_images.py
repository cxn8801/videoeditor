import os
from moviepy.editor import *

def extract_frames(movie, imgdir):
    clip = VideoFileClip(movie)
    duration = clip.duration
    print(duration / 60)
    t = 0
    while t < duration:
        imgpath = os.path.join(imgdir, '{}.png'.format(t))
        clip.save_frame(imgpath, t)
        t += 0.05

movie = '1.mp4'
imgdir = 'frames'
# times = 0.1, 0.63, 0.947, 1.2, 3.8, 6.7

extract_frames(movie, imgdir)