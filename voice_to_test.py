# -*- coding: utf-8 -*-
import speech_recognition as sr
import goslate

r = sr.Recognizer()
gs = goslate.Goslate()

def voice_to_test(voice):
    """convert different languages voices to test
    and convert test to english test
    """
    try:
        res  = r.recognize_google(voice,language = 'hi-IN')
    #    res2  = "Test: " +r.recognize_google(audio)
        print(res)
        translatedText = gs.translate(res,'en')
        return translatedText
    except:
        pass;

#print(voice_to_test.__doc__ )