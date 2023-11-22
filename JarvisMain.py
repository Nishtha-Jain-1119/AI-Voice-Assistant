from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer 
from Body.Listen import MicExecution 
print("\n>> Starting the Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExe
print(">> Starting the Jarvis : Wait For Few More Seconds, Please.")


def MainExe():

    Speak("Hello Sir")
    Speak("I am Jarvis, I'm ready to assist you.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")


        if len(Data)<3:
            pass

        elif "stop" in Data:
            break

        elif MainTaskExe(Data):
            pass

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
        

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        MainExe()        

# calling clapdetect function to execute MainExe
ClapDetect()

        # elif "calculate" in Data or "answer" in Data or "solve" in Data or "solution" in Data or "question" in Data:
        #     Reply1 = QuestionAnswer(Data)
        #     Speak(Reply1)