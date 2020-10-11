import webbrowser
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

print("welcome to my tools")
pyttsx3.speak("welcome to my tools")


print("enter ur requirements:")

with sr.Microphone() as source:
    print('start say ....')
    audio = r.record(source,duration=4)
    print('speech done')

ch=r.recognize_google(audio)
print(ch)
if "date" in ch:
	webbrowser.open("http://"ip address"/cgi-bin/1.py?c=date")
elif "calendar" in ch:
	webbrowser.open("http://"ip address"/cgi-bin/1.py?c=cal")
elif ("search" in ch) and ("Google" in ch):
	webbrowser.open("https://google.com/?q=%s"%(ch))
else:
	print("not understand")

