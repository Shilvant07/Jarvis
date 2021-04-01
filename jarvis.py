import pyttsx3
import datetime
import speech_recognition as sr  # for voice recognition
import wikipedia                 # first install wikipedia then import
import webbrowser                # inbuild hota hai use for open any websites
import os                        # for internal operation.

engine = pyttsx3.init('sapi5')             # use for inbuild voice commond api  dene keliye
voices = engine.getProperty('voices')      #print(voices)# check voices there are two vices are availbe in my laptop zera and devid.
engine.setProperty('voices',voices[1].id)

def speak(audio):                          # speak funcion to create voice assistent
    engine.say(audio)
    engine.runAndWait()

def wishMe():    # for wishing AI
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Shilvant")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Shilvant:")
    else:
        speak("Good Evening Shilvant")
    speak("I am Jarvis Sir. Please tell me how may i help you")  # speak function call kiya taki jarivs apne bareme bata sake.

def tekCommond():
    # i takes microphonne input into user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                     # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')    # user voice  language recognze
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again please..")                      # agar koi error aata hai usko handle karne ke liye.
        return "None"
    return query

if __name__ in "__main__":
    wishMe()
    while True:
    #if 1:
        # logic foor executin tasks based on query
        query = tekCommond().lower()                         # query ko lower case me convert karta hai.
        if 'wikipedia' in query:                             # check karega query ko wikipedia mila ya nahi
            speak("searching Wikipedia..")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)    # wikipedia me se kitne sentense AI read karega oh apne upar hai.
            speak("According to Wikipedia")
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Shil\\Music\\Bhim song'    # music ka path set karna hai jaha par music folder hai.
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is{strtime}")

        elif 'open code' in query:
            code_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(code_path)
        elif 'exit' in query:
            exit()