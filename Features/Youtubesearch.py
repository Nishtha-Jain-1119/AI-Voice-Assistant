import webbrowser
import pywhatkit

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
        elif "on" in data:
            data = data.replace("on", "")
        elif "do" in data:
            data = data.replace("do", "")
        elif "then" in data:
            data = data.replace("then", "")
        elif "alright" in data:
            data = data.replace("alright", "")
        elif "you" in data:
            data = data.replace("you", "")
        elif "tube" in data:
            data = data.replace("tube", "")
        elif "search" in data:
            data = data.replace("search", "")
        elif "video" in data:
            data = data.replace("video", "")
        elif " " in data:
            data = data.replace(" ", "")
        else:
            break
    return data

def Youtube(query):
    query = str(query).lower()
    query = RemoveExtraText(query)
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open_new_tab(web)
    pywhatkit.playonyt(query)
    return True

# Youtube("Ok jarvis now search ye desh h veer jawano ka")