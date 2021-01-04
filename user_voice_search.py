# -*- coding: utf-8 -*-
import speech_recognition as sr

r = sr.Recognizer()

def speak():
    """Read the user voice till 4 sec
    and avoid different noises.
    """
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source,timeout=1,phrase_time_limit=4)
        r.adjust_for_ambient_noise(source,duration=0.515)
        return audio
        print("time Over ,Thanks")
#print(speak.__doc__ )