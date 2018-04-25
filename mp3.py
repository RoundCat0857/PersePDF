from gtts import gTTS
fp=open('final.txt','r')
contents = fp.read()
fp.close()
tts = gTTS(text=contents, lang='en')
tts.save("final.mp3")
