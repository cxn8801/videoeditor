# importing the required packages
import pyautogui
import cv2
import numpy as np
import pyaudio
import wave
from threading import Thread
from pynput.mouse import Listener as Mouse_Listener
from pynput.keyboard import Key
from pynput.keyboard import Listener as Keyboard_Listener

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "some_video.avi"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 15

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
# cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
# cv2.resizeWindow("Live", 480, 270)


# 声音相关
# Record in chunks of 1024 samples
chunk = 1024

# 16 bits per sample
sample_format = pyaudio.paInt16
chanels = 2

# Record at 44400 samples per second
smpl_rt = 44400
seconds = 3600 * 100
stop = False
filename = "some_audiofile.wav"

# Create an interface to PortAudio
pa = pyaudio.PyAudio()

stream = pa.open(format=sample_format, channels=chanels,
				rate=smpl_rt, input=True,
				frames_per_buffer=chunk)

# print('Recording...')

# Initialize array that be used for storing frames
frames = []

def audio_record():
	# Store data in chunks for 8 seconds
	for i in range(0, int(smpl_rt / chunk * seconds)):
		data = stream.read(chunk)
		frames.append(data)
		if stop:
			break

	# Stop and close the stream
	stream.stop_stream()
	stream.close()

	# Terminate - PortAudio interface
	pa.terminate()

	print('Done !!! ')

	# Save the recorded data in a .wav format
	sf = wave.open(filename, 'wb')
	sf.setnchannels(chanels)
	sf.setsampwidth(pa.get_sample_size(sample_format))
	sf.setframerate(smpl_rt)
	sf.writeframes(b''.join(frames))
	sf.close()

audio_record_thread = Thread(target = audio_record)
audio_record_thread.start()


from moviepy.editor import *

def on_press(key):  
    # 监听按键
    print('{0} pressed'.format(key))
 
def on_release(key):
    global stop
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:     
        stop = True
        keyboard_listen_thread.stop()
        audio_record_thread.join()
		# Release the Video writer
        out.release()

		# Destroy all windows
        # cv2.destroyAllWindows()

        audioclip = AudioFileClip("some_audiofile.wav")
        videoclip = VideoFileClip("some_video.avi")
        videoclip2 = videoclip.set_audio(audioclip)
        videoclip2.write_videofile('result.mp4')


# 连接事件以及释放
keyboard_listen_thread = Keyboard_Listener(on_press=on_press, on_release=on_release)
keyboard_listen_thread.start()



while True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	if stop == True:
		break

	# # Optional: Display the recording screen
	# cv2.imshow('Live', frame)
	
	# # Stop recording when we press 'q'
	# if cv2.waitKey(1) == ord('q'):
	# 	stop = True
	# 	t.join()
	# 	break

keyboard_listen_thread.join()
