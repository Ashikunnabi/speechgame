# dependencies:
# pip install pyaudio
# pip install google-api-python-client
# pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Say Something!')
    audio = r.listen(source)
    print('Done!')
    
try: 
    text = r.recognize_google(audio)
    print(text)
    
except Exception as e:
    print(e)
