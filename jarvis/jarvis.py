import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import psutil

# Initialize the engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant, Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return None
    except sr.RequestError:
        speak("Speech service is down.")
        return None

def process_query(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("I couldn't find anything on Wikipedia.")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'day' in query:
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}")

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'search' in query:
        speak("What should I search for?")
        search_query = take_command()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching Google for {search_query}")
            webbrowser.open(url)

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        speak(joke)

    elif 'battery' in query:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            speak(f"Battery is at {percent} percent")
        else:
            speak("Battery information not available.")

    elif 'weather' in query:
        speak("Opening weather forecast")
        webbrowser.open("https://www.google.com/search?q=weather")

    elif 'exit' in query or 'stop' in query:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I didn't understand that command.")

    return True


if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()
        if command:
            if not process_query(command):
                break
