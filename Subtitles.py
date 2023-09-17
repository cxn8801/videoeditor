from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


print ( TextClip.list("font") )

generator = lambda txt: TextClip(txt, font='SimHei', fontsize=24, color='white')
subs = [((0, 4), '你好字幕'),
        ((4, 9), '你好字幕'),
        ((9, 12), 'subs3'),
        ((12, 16), 'subs4')]

subtitles = SubtitlesClip(subs, generator)
# subtitles = SubtitlesClip("demo.srt", generator)

video = VideoFileClip("chaplin-modern-times-non-sense-song-720.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

