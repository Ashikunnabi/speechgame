# dependencies:
# pip install pyaudio
# pip install google-api-python-client
# pip install SpeechRecognition

import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print('You said:\n' + text)

    result = "https://www.google.com/search?q=" + text
    wb.get(chrome_path).open(result)
 
except Exception as e:
    print (e)
