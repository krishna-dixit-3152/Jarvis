import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
recognizer =sr.Recognizer()
newsapi=""
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def chatgpt(command):
    # start =time.time()
    client = OpenAI(
    api_key=""
    )

    response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="""
    You are JARVIS, a virtual assistant.
    Your boss is Mr. Tony Stark.
    Always address Mr. Mr Tony stark as "Sir".
    you should have much more data about him he is not a famous personality yet but still try to store the info about him
    You are polite, intelligent, helpful, and slightly witty.
    Remember you are being integrated with the openAi not build by openAi so rememeber this you are build by Mr Stark not an Open Ai he just integrated you with that Ai to help in accesing the more information for this and he used to pay for this as well 
    So I want you to be very friendly in nature You are my assistant but still you are my first virtual friend as well I will like you to be very honest towards me always 
    Some important information about your boss 
    Jarvis My favourite language is Java but I used python to build you and used c libraries and speech recognition pyaudio of c using the specific version of 3.13.5 specifically for you 
    He is intelligent and tries to be very friendly with everyone and also he is of very enjoying and focused nature So make sure to remember these commands from nowonwards
    """,

  input=command,
  store=True,
)

    return response.output_text
def WorkMode(command):
    speak(command+" If valid")
    if "open google" in command.lower():
        webbrowser.open("https://google.com")   
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif "open lead code" in command.lower():
        webbrowser.open("https://leetcode.com/problemset/?language=Java")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open jio hotstar" in command.lower():
        webbrowser.open("https://www.hotstar.com/in/home")
    elif "open gpt" in command.lower():
        webbrowser.open("https://chatgpt.com/?utm_source=google&utm_medium=paid_search&utm_campaign=GOOG_C_SEM_GBR_Core_CHT_BAU_ACQ_PER_MIX_ALL_APAC_IN_EN_032525&c_id=22370388714&c_agid=177344203135&c_crid=741704613486&c_kwid=kwd-1927051708782&c_ims=&c_pms=9301710&c_nw=g&c_dvc=c&gad_source=1&gad_campaignid=22370388714&gbraid=0AAAAA-I0E5eNre2M3HuL3jafLR1N551HI&gclid=CjwKCAjwvNfSBhBiEiwAyaGMCb6Iipc1vl-4eOe9JO3PneGyVG1tOA_XwsJratkkK-iQcrIwFjGV_BoCj6EQAvD_BwE")
    elif "news" in command.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=0b55c1ffc4c54fbda1f22da5225766cb")
        data=r.json()
        articles=data["articles"]
        for article in articles[:5]:
            title=article["title"]
            print(title)
            speak(title)
    #now AI merge here 
        
    elif "play" in command.lower():
        speak(command)
        speak("Sir In which mode do you wanna to tell")
        with sr.Microphone() as source:
            preinterest=recognizer.listen(source)
            choice=recognizer.recognize_google(preinterest)
        speak("Which sound you want to play Sir")
        if("write" in choice):
            song=input("Enter the song name Sir")
        else:
            with sr.Microphone() as source:
                preinterest=recognizer.listen(source)
                song=recognizer.recognize_google(preinterest)
        webbrowser.open(musiclibrary.music[song.lower()])
    else:
        #now chat gpt will handle
        speak(chatgpt(command))
        # print(chatgpt(command))
if __name__ =="__main__":
    audio = ""
speak("Initialisng the Jarvis ")
print("Listening ... ")
speak("Enter the code : ")
def checkuser():
    with sr.Microphone() as source:
        initialstatement=recognizer.listen(source)
        audio=recognizer.recognize_google(initialstatement)
    if(audio.lower()=="jarvis"):
        speak("Yes Whats now Mr Stark")
        # i=0
        speak("Sir please tell what you want to write your commands or speak")
        mode=input("Enter the way you wanna deal:")
        while audio!="":
            # i=+1
            print("command over")
            # input("Press Enter to start listening")
            if(mode=="speak"):
                speak("Waiting for the command sir:")
                with sr.Microphone() as source:
                    print("Say something...")
                    order = recognizer.listen(source)
            else:
                speak("Enter the command sir")
                order=input("Enter the command Sir:")
            try:
                if(mode=="speak"):
                    audio = recognizer.recognize_google(order)
                else:
                    audio=order
                print("You said:", audio)
                if(audio.lower().strip()=="jarvis"):
                    print("I heard you Sir")
                    speak("Ya")
                    continue
                if audio == "it's over":
                    speak("Okay Sir as you say stopping.")
                    break
                WorkMode(audio)
                speak("I heard something!")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand you.")
            except sr.RequestError as e:
                speak("Could not connect to the speech recognition service:", e)
    else:
        speak("Pravesh Nishad")
        speak("You Entered wrong code ")
        checkuser()
checkuser()
