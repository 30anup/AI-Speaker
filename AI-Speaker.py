import os
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
if __name__=="__main__":
    print("Welcome to AI-Speaker 1.1 Created By Anup Nair")
    while True:
        Anup=input("Enter What you want to Speak:-")
        if Anup=="bye":
            speak.speak("bye bye friend")
            break
        command=f"{Anup}"
        speak.speak(command)


