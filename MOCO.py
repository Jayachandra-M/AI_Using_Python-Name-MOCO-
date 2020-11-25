import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import geocoder
import requests
import json


g = geocoder.ip('me')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])

def wishMe():
    speak("Hey Jai Welcome Back!")
    time()
    date()
    weather()
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning jai")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon jai")

    else:
        speak('Good Evening jai')

    speak("Moco at your service,what do you want me to do?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"     
    return query
def screenshot():
    img = pyautogui.screenshot()
    img.save('screenshot.png')
def webcamsnap():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ehacking07@gmail.com", "thereisnoplacelike127.0.0.1")
    server.sendmail('ehacking07@gmail.com', to, content)
    server.close()
def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' + data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        speak('Humidity is ' + str(main['humidity']))


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            speak("the current time is")
            time()
        elif 'date' in query:
            speak("today's date is")
            date()
        elif 'what is the weather' in query or 'weather' in query:
            speak("the weather now is")
            weather()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'turn on bluetooth' in query:
            speak("turning on bluetooth")
            os.system("rfkill unblock bluetooth")
        elif 'turn off bluetooth' in query:
            speak("turning off bluetooth")
            os.system("rfkill block bluetooth")

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = 'recepient email' #receiver email 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send the email")
        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'shutdown' in query:
            os.system("shutown /s /t 1") 
        elif 'restart' in query or 'restat' in query:
            os.system('shutdown /r /t 1')
        elif 'logout' in query or 'log out' in query:
            os.system('shutdown -1')
        elif 'moco are you there' in query:
            speak("Yes Sir, at your service")
        elif 'goodbye' in query or 'good boy' in query or 'goodboy' in query:                          
            speak("Goodbye jai moco is powering off in 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 Bye")
            break
        elif 'thanks' in query or 'tanks' in query or 'thank you' in query:
            speak('You are wellcome', 'no problem')
        elif 'who developed you' in query:
            if platform == "win32" or "darwin":
                speak('jayachandra is my master. He created me on 26th october 2020')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')
        elif 'what is your name' in query:
            speak('My name is Moco')

        elif 'moco stands for' in query:
            speak('MOCO stands for Hacker who can get into your data without knowing to you')
        elif 'shutdown' in query:
            speak('good night')
            os.system('Shutdown.exe -s -t 00')

        elif 'restart' in query:
            speak("restarting")
            os.system("Shutdown.exe -r -t 00") 

        elif "open whatsapp" in query or "whats hub" in query:
            speak("opening whats app")
            webbrowser.open_new_tab("https://web.whatsapp.com")

        elif "open instagram" in query:
            speak("Opening instagram")
            webbrowser.open_new_tab("https://instagram.com")

        elif "open facebook" in query:
            speak("Opening facebook")
            webbrowser.open_new_tab("https://facebook.com")

        elif "open uimart" in query or 'open UI mode' in query or 'open my mart' in query or 'open uae mart' in query or 'open UI Mart' in query:
            speak("opening Uimart")
            webbrowser.open_new_tab("https://www.uimart.in/admin/order")

        elif 'play songs' in query:
            songs_dir = '' #songs directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()
        elif 'snapshot' in query or 'snapchat' in query:
            speak("taking webcam picture")
            webcamsnap()
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'cpu' in query:
            speak("Loading...")
            cpu()
        elif 'jokes' in query or 'joke' in query:
            speak("here is a joke")
            joke()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())
        elif 'offline' in query:
            quit()
        

    