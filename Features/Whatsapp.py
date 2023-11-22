import sys
sys.path.append("C:\\Users\\njish\\OneDrive\\Desktop\\AI Voice Assistant")
from Body.Listen import Listen
from Body.Speak import Speak
from Database.contactList import List

import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(msg: str,phone_no: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            
            phone_no=phone_no, 
            message=msg,
            tab_close=True
        )
        time.sleep(5)
        pyautogui.click()
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        Speak("Message sent!")
    except Exception as e:
        print(str(e))


def RemoveExtraText(data):
    while True:
        if "jarvis" in data:
            data = data.replace("jarvis", "")
        elif "ok" in data:
            data = data.replace("ok", "")
        elif "now" in data:
            data = data.replace("now", "")
        elif "fine" in data:
            data = data.replace("fine", "")
        elif "can" in data:
            data = data.replace("can", "")
        elif "please" in data:
            data = data.replace("please", "")
        elif "you" in data:
            data = data.replace("you", "")
        elif "so" in data:
            data = data.replace("so", "")
        elif "to" in data:
            data = data.replace("to", "")
        elif "ok" in data:
            data = data.replace("ok", "")
        elif "then" in data:
            data = data.replace("then", "")
        elif "alright" in data:
            data = data.replace("alright", "")
        elif "send" in data:
            data = data.replace("send", "")
        elif "whatsapp" in data:
            data = data.replace("whatsapp", "")
        elif "message" in data:
            data = data.replace("message", "")
        elif "chat" in data:
            data = data.replace("chat", "")
        elif "with" in data:
            data = data.replace("with", "")
        elif " " in data:
            data = data.replace(" ", "")
        else:
            break
    return data

def Whatsapp(query):
    name = RemoveExtraText(query)
    print(name)
    phone_no = List[name]
    print(phone_no)
    Speak("What should I send by the way?")
    msg = Listen()
    send_whatsapp_message(msg=msg,phone_no=phone_no)
    return True
    

Whatsapp("jarvis, send message to papa")
