import pyttsx3
friend = pyttsx3.init()
speech = input ("Enter something: ")
friend.say(speech)
friend.runAndWait()
