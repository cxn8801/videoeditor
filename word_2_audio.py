import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty("voices")
print(voices)

# engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
# convert this text to speech

with open('readme.txt', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        # print(line.strip())
        engine.say(line)

engine.save_to_file('Hello World', 'test.mp3')

# play the speech
engine.runAndWait()