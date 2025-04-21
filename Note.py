# pip install speechrecognition
# pip install pyaudio
# pip install pyttsx3

import speech_recognition as sr
import pyttsx3 

# This function takes input from your microphone and returns what it thinks you said.
# It gets an error a lot but it will keep calling the function until it works.
def get_text_from_speech():
    r = sr.Recognizer() 
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            audio = r.listen(source2)
            
            phrase = r.recognize_google(audio)
            phrase = phrase.lower()
            
            print(phrase)
            return phrase
            
    except sr.RequestError as e:
        print("Could not request results {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
        return get_text_from_speech()


# get_text_from_speech()
