import pyttsx3 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

#creating the speak engine using pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voices', voices[0].id)

global text;


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("helo sir i am LUCIFER.")
    speak("Please tell me how may I help you") 

 
def takeCommand(text_incoming):
    global text
    
    text=text_incoming.lower()
    start()
    

def mailcontent():
    global text;
    
    content=text.lower()
    conent = content.replace("mail ","")
    to = "xxxxxx@gmail.com"    
    sendEmail(to, content)
    speak("Email has been sent!")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xxx@gmail.com', '$hubham17')
    server.sendmail('xxxxxx@gmail.com', to, content)
    server.close()

# the created data set
def start():
    
    #while True:
     if 1:
        global text
        # Logic for executing tasks based on text
        
        if 'wiki' in text:
            speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            
            results = wikipedia.summary(text, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in text:
             webbrowser.open("youtube.com")
             speak(" Sir,opening youtube")

        elif 'google' in text:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'stackoverflow' in text:
            webbrowser.open("stackoverflow.com")
            speak("Sir,opening stackoverflow")

        elif 'gmail' in text:
            webbrowser.open("gmail.com")
            speak("Sir,opening gmail")

        elif 'bcet' in text:
            webbrowser.open("bcetgsp.ac.in")
            speak(" Sir,opening beant college of engenineering and technology website")
    

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            

            
        elif 'music' in text:
            music =r'C:\Users\FROSTBITE\Desktop\music'
            songs = os.listdir(music)
            print(songs)
            speak(" sir, playing music")
            os.startfile(os.path.join(music, songs[0]))

        elif 'video' in text:
            video =r'C:\Users\FROSTBITE\Desktop\video'
            songs = os.listdir(video)
            print(songs)
            speak("playing teqfest video")
            os.startfile(os.path.join(video, songs[0]))    

        elif 'mail' in text:
            try:
                speak("Sending")
                mailcontent()
                
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    

        else:
             speak("sorry sir i am a learning bot , i did not get u there")

