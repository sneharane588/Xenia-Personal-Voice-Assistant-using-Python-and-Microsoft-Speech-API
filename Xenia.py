import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices)
engine.setProperty('voice', voices[1].id)
# print(voices[0].id) # male
# print(voices[1].id) # female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning !")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am Xenia, Your Personal voice assistant, How can I help You mam?")


def takeCommand():
    '''
     accepts microphone i/p and returns str o/p
    '''    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print('Recognizing')
        query=r.recognize_google(audio, language='en-in')
        # print('User said : ', query)
        print(f"Here are the results for : {query}\n")
        
    except Exception as e:
        # print(e)
        print("Please, Say that again mam")
        speak("Please, Say that again mam")
        return "None"
    return query
    
if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()
        # executing tasks as said in query
        if 'wikipedia' in query:
            speak('Searching Wikipedia : ')
            query = query.replace("wikipedia", "") # remove the word wikipedia from query
            res = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia, ')
            print(res)
            speak(res)
        elif (('open' or 'run' or 'play' or 'goto') and 'youtube') in query:
            wb.open('youtube.com')
        elif (('open' or 'goto') and 'github') in query:
            wb.open('github.com')
        elif (('open' or 'goto') and ('mail' or 'email')) in query:
            wb.open('gmail.com')
        elif (('open' or 'goto') and 'stack overflow') in query:
            wb.open('stackoverflow.com')
        elif ('play' and ('music' or 'the music' or 'a song')) in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            random = random.randrange(0, len(songs)-1) 
            os.startfile(os.path.join(music_dir, songs[random]))
        elif 'time' in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {t}")        
        elif 'open chrome' in query:
            os.system('chrome')        
        elif (('open' or 'execute' or 'run' or 'goto') and ('notepad')) in query:
            os.system('notepad')
                      



