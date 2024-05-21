import pyttsx3   
import speech_recognition as sr
import datetime
import wikipedia 
import os
import webbrowser


#Take voice from my system

engine = pyttsx3.init('sapi5')    #SAPI5 is Microsoft Speech API 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 for Male Voice and 1 for Female Voice
engine.setProperty('rate',150)   #Speech Rate
engine.setProperty('volume',1)   #Speech Volume


#SPEECH FUNCTIONS ------------------------
def speak(text):
    """This function takes text and returns voice 

    Args:
        text (_type_): string   
    """
    engine.say(text)
    engine.runAndWait()

# speak("Hello, I am a Data Scientist")


#SPEECH RECOGNIZATION ----------------------------------------------------------------
def takeCommand():
    """This function takes voice and returns text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   # Waits for 1 second of silence before ending the sentance 
        r.listen(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
#Wish me on time Function

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Pranita!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Pranita!")
    else:
        speak("Good Evening Pranita!")
    speak("I am at your service. Please tell me how can I help you")

# text =takeCommand()
# speak(text)

if __name__ == "__main__":

    wishMe()

    while True:    #continous listening 

        query = takeCommand().lower()
        # print(query)

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Open youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Open google")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("Open stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open facebook" in query:
            speak("Open facebook")
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            speak("Open instagram")
            webbrowser.open("instagram.com")

        elif "open linkedin" in query:
            speak("Open linkedin")
            webbrowser.open("linkedin.com")

        elif "open github" in query:
            speak("Open github")
            webbrowser.open("github.com")
        
        elif "date" in query:  
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"Sir, the date is {strDate}")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "goodbye" in query:
            speak("Goodbye Pranita!")
            exit()




    

