import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


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
        elif "for" in data:
            data = data.replace("for", "")
        elif "me" in data:
            data = data.replace("me", "")
        elif "then" in data:
            data = data.replace("then", "")
        elif "the" in data:
            data = data.replace("the", "")
        elif "alright" in data:
            data = data.replace("alright", "")
        elif "website" in data:
            data = data.replace("website", "")
        elif " " in data:
            data = data.replace(" ", "")
        else:
            break
    return data


def OpenExe(query):
    query = str(query).lower()
    query = RemoveExtraText(query)

    if "visit" in query:
        Nameof_web = query.replace("visit", "")
        Link = f'https://www.{Nameof_web}.com'
        webbrowser.open(Link)
        return True

    elif "goto" in query:
        Nameof_web = query.replace("goto", "")
        Link = f'https://www.{Nameof_web}.com'
        webbrowser.open(Link)
        return True

    elif "open" in query:
        Nameof_app = query.replace("open", "")
        if "brave" in Nameof_app:
            os.startfile(
                r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        elif "chrome" in Nameof_app:
            os.startfile(
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        else:
            pyautogui.press('win')
            keyboard.write(Nameof_app)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
        return True

    elif "launch" in query:
        Nameof_app = query.replace("launch", "")
        if "brave" in Nameof_app:
            os.startfile(
                r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        elif "chrome" in Nameof_app:
            os.startfile(
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        else:
            pyautogui.press('win')
            keyboard.write(Nameof_app)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
        return True

    elif "start" in query:
        Nameof_app = query.replace("start", "")
        if "brave" in Nameof_app:
            os.startfile(
                r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        elif "chrome" in Nameof_app:
            os.startfile(
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        else:
            pyautogui.press('win')
            keyboard.write(Nameof_app)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
        return True

# OpenExe("now go to leetcode")