import pyttsx3
import speech_recognition
import enchant
import keyboard

from assistant_service import assistantModel

voiceAssistant = pyttsx3.init()
voices = voiceAssistant.getProperty("voices")
voiceAssistant.setProperty("voice", voices[1].id)

checkEn = enchant.Dict("en_US")

def checkEnService(content) -> bool:
    temp = content.split()
    count_vi = 0
    count_en = 0
    for i in temp:
        if checkEn.check(i):
            count_en += 1
        else:
            count_vi += 1
    
    if  count_vi < count_en:
        return True
    
    return False

def assistantSpeak(audio):
    voiceAssistant.say(audio)
    voiceAssistant.runAndWait()

def userCommand():
    assistant_ear = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        assistant_ear.dynamic_energy_threshold = True
        assistant_ear.dynamic_energy_adjustment_damping = 0.5
        assistant_ear.dynamic_energy_adjustment_ratio = 1.5

        audio = assistant_ear.listen(mic)
        assistant_ear.phrase_threshold = 10

    try:
        query = assistant_ear.recognize_google(audio, language='vi')
    except:
        query = ""
    
    return query

def assistant():
    print("Assistant: Hệ thống đã được bật.")
    assistantSpeak("Hệ thống đã được bật.")
    query = userCommand().lower()

    while True:
        print("User: " + query)
        if (("nhóm 4" in query) or ("nhóm bốn" in query) or ("54" in query)):
            assistantSpeak("Tôi nghe đây.")
            query = userCommand().lower()
            print("User: " + query)
            if checkEnService(query):
                answer = "Xin lỗi tôi không hiểu tiếng anh."
            else:
                answer = assistantModel(query)
            assistantSpeak(answer)
            print("Assistant: " + answer)

            if answer == "Tạm biệt và hẹn gặp lại.":
                print("Assistant: Hệ thống đã được tắt.")
                assistantSpeak("Hệ thống đã được tắt.")
                return
        else:
            query = userCommand().lower()

if __name__ == "__main__":
    while True:
        if keyboard.read_key() == "space":
            assistant()
        if keyboard.read_key() == "esc":
            break