import pickle

from moviepy import *
from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking
from moviepy.video.tools.tracking import Trajectory
import cv2


print(cv2.__version__) 

# LOAD THE CLIP (subclip 6'51 - 7'01 of a chaplin movie)
clip = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4").subclip(20, 25)

# MANUAL TRACKING OF THE HEAD

# the three next lines are for the manual tracking and its saving
# to a file, it must be commented once the tracking has been done
# (after the first run of the script for instance).
# Note that we save the list (ti,xi,yi), not the functions fx and fy
# (that we will need) because they have dependencies.

# txy = manual_tracking(clip, fps=5, savefile="track.txt")
# print(txy)
# print(list(txy[0].txy()))

# traj = Trajectory.load_list('track.txt')
# print(traj)
# print(traj[0].txy())
# print(list(traj[0].txy()))

# with open("chaplin_txy.dat",'wb') as f:
#    pickle.dump(txy, f, protocol=pickle.HIGHEST_PROTOCOL)



# IF THE MANUAL TRACKING HAS BEEN PREVIOUSLY DONE,
# LOAD THE TRACKING DATA AND CONVERT IT TO FUNCTIONS x(t),fy(t)

# with open("chaplin_txy.dat",'rb') as f:
#     # fx,fy = to_fxfy( pickle.load(f) )
#     txy = pickle.load(f)
#     # Trajectory.load_list(txy)
#     print(txy.txy())


def f_x(t):
    return 0

def f_y(t):
    return 0

# BLUR CHAPLIN'S HEAD IN THE CLIP

# clip_blurred = clip.fx( vfx.headblur, traj., f_y, 25)

manual_tracking(clip, fps=6, savefile="blurred_trajectory.txt")
traj = Trajectory.from_file("blurred_trajectory.txt")

print(traj.xi)
print(traj.yi)

clip_blurred = clip.fx(vfx.headblur, traj.xi, traj.yi, 40)


# # Generate the text, put in on a grey background

# txt = TextClip("Hey you ! \n You're blurry!", color='grey70',
#                size = clip.size, bg_color='grey20',
#                font = "Century-Schoolbook-Italic", fontsize=40)
               
               
# Concatenate the Chaplin clip with the text clip, add audio

final = concatenate_videoclips([clip_blurred]).set_audio(clip.audio)

# We write the result to a file. Here we raise the bitrate so that
# the final video is not too ugly.

final.write_videofile('blurredChaplin.mp4')