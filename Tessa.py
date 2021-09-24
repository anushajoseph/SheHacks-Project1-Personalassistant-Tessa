import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hey I am Tessa')
engine.say('How can I help you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening ......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa'in command:
                command = command.replace('alexa', '')
                print(command)
        return command
    except:
        pass


def run_tessa():
        command = take_command()

        print(command)
        if 'play' in command:
            song = command.replace('play','')
            talk('playing'+song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        else:
            talk('Please say the command again')

while True:
        run_tessa()