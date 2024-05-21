import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS 
import os


GOOGLE_API_KEY = ****************************************
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    '''
    code captures audio input from the microphone, processes it using Google Speech Recognition
    and returns the text.
    '''
    r = sr.Recognizer()               # create instance of recognizer
    with sr.Microphone() as source:   # microphone for capturing audio.
        print("Listening........")
        audio = r.listen(source)    #this listens to the audio from the microphone and stores it in the audio variable.
    try:
        text = r.recognize_google(audio)  #instance to recognize the speech from the audio and convert it to text
        print("You said:",text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't get that")
    except sr.RequestError as e:    
        print("Couldn't request reults from Google Speech Recognition Service {0}".format(e))


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")
   

def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro') #creates an instance of the GenerativeModel class, model named 'gemini-pro' is selected.
    response = model.generate_content(user_text)
    result = response.text 
    return result





 