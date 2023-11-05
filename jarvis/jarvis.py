import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import audioop


engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour==0 and hour==12:
        speak("Good morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    
    else:
        speak("Good evening!")

    speak('I am YOUR Personal assistant sir!')

def takeCommand():
    #it takes microphone input and rreturn string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("recognizing...")
        query = r.recognize_bing(audio,language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        #print(e)
        print("say something again...")
        return "None"
    return query
    

if __name__ =='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        if wikipedia in query :
            speak('Sarching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
