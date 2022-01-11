import speech_recognition as sr

r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                      
    print("listening...")
    audio = r.record(source,duration=3)
    try:
        str=r.recognize_google(audio)
        str= str.lower()
        if 'jarvis' in str:
            print(str)
    except:
        print("some error occurred!")