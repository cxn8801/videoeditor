
# Import everything needed to edit video clips
from moviepy.editor import *
 
# loading video dsa gfg intro video and getting only first 5 seconds
clip1 = VideoFileClip("input.mp4").subclip(0, 5)
 
# rotating clip1 by 90 degree to get the clip2
clip2 = VideoFileClip("input.mp4").subclip(19, 24)
 
# rotating clip1 by 180 degree to get the clip3
clip3 = VideoFileClip("input.mp4").subclip(40, 45)
 
# rotating clip1 by 270 degree to get the clip4
clip4 = VideoFileClip("input.mp4").subclip(60, 70)
 
clip4 = clip4.resize(1.5)
 
# list of clips
clips = [[clip1, clip2],
        [clip3, clip4]]
 
 
# stacking clips
final = clips_array(clips)

audioclip = AudioFileClip("1.mp3").subclip(0, 5) 
# adding audio to the video clip 

temp_audio_clip = final.audio.volumex(0.5)
final_audio = CompositeAudioClip([temp_audio_clip, audioclip])
final = final.set_audio(final_audio) 
# final = final.set_audio(audioclip) 



final.write_videofile('result.mp4')


# showing final clip
final.ipython_display(width = 480)
