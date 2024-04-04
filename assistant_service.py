from openai import OpenAI
import datetime
import requests

api_link = "https://84f66vbk-3000.asse.devtunnels.ms"  # Replace with your actual API URL
client = OpenAI(api_key="") #API openAI

def control_API(api_link, led_topic, action):
  url = f"{api_link}/api/control/{action}"  # Construct the full URL
  headers = {'Content-Type': 'application/json'}
  data = {'topic': led_topic}  # Payload data for the PUT request

  try:
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response
  except requests.exceptions.RequestException as error:
    print(f"Error controlling LED: {error}")
    return None

def gptService(userContent):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a useful virtual assistant in the smart home."},
            {"role": "system", "content": "Our house is at Vietnam Aviation Academy campus 2."},
            {"role": "system", "content": "You answer briefly in one sentence."},
            {"role": "user", "content": userContent}
        ],
            max_tokens=271, 
            n=1,
            temperature=1
    )

    return response.choices[0].message.content

def time():
    timeCurrent = [datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year]
    
    return timeCurrent  

statusLightAndFan = [0, 0] #đèn, quạt

def assistantModel_vi(userContent):
    if userContent == "":
        answer = "Xin lỗi, tôi không nghe rõ"
    elif (("quạt" in userContent) or ("đèn" in userContent)) or (("quat" in userContent) or ("den" in userContent)):
        if (("bật" in userContent) and ("quạt" in userContent) and ("đèn" in userContent)) or (("bat" in userContent) and ("quat" in userContent) and ("den" in userContent)):
            answer = "Tôi đã bật quạt và đèn."

            response = control_API(api_link, "led01", "led-on")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "led02", "led-on")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "fan01", "fan-on")
            if response:
                print("FAN turned on successfully!")
            response = control_API(api_link, "fan02", "fan-on")
            if response:
                print("FAN turned on successfully!")
        elif (("tắt" in userContent) and ("quạt" in userContent) and ("đèn" in userContent)) or (("tat" in userContent) and ("quat" in userContent) and ("den" in userContent)):
            answer = "Tôi đã tắt quạt và đèn."

            response = control_API(api_link, "led01", "led-off")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "fan01", "fan-off")
            if response:
                print("FAN turned on successfully!")
            response = control_API(api_link, "led02", "led-off")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "fan02", "fan-off")
            if response:
                print("FAN turned on successfully!")
        elif (("bật" in userContent) and ("đèn" in userContent)) or (("bat" in userContent) and ("den" in userContent)):
            answer = "Tôi đã bật đèn."

            response = control_API(api_link, "led01", "led-on")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "led02", "led-on")
            if response:
                print("LED turned on successfully!")
        elif (("tắt" in userContent) and ("đèn" in userContent)) or (("tat" in userContent) and ("den" in userContent)):
            answer = "Tôi đã tắt đèn."

            response = control_API(api_link, "led01", "led-off")
            if response:
                print("LED turned on successfully!")
            response = control_API(api_link, "led02", "led-off")
            if response:
                print("LED turned on successfully!")
        elif (("bật" in userContent) and ("quạt" in userContent)) or (("bat" in userContent) and ("quat" in userContent)):
            answer = "Tôi đã bật quạt."

            response = control_API(api_link, "fan01", "fan-on")
            if response:
                print("FAN turned on successfully!")
            response = control_API(api_link, "fan02", "fan-on")
            if response:
                print("FAN turned on successfully!")
        elif (("tắt" in userContent) and ("quạt" in userContent)) or (("tat" in userContent) and ("quat" in userContent)):
            answer = "Tôi đã tắt quạt."

            response = control_API(api_link, "fan01", "fan-off")
            if response:
                print("FAN turned on successfully!")
            response = control_API(api_link, "fan02", "fan-off")
            if response:
                print("FAN turned on successfully!")
        else:
            answer = "Tôi có thể điều chỉnh trạng thái hai thiết bị này, bạn có thể nói rõ ràng hơn."
        
    elif ("chào" in userContent) or ("chao" in userContent):   
        answer = "Xin chào, tôi là trợ lý ảo nhà thông minh."
    elif ((("mấy" in userContent) or ("nhiêu" in userContent) or ("khoảng" in userContent) or ("hiện" in userContent)) 
          and (("giờ" in userContent) or ("thời gian" in userContent) or ("phút" in userContent) or ("giây" in userContent))) or ((("may" in userContent) or ("nhieu" in userContent) or ("khoang" in userContent) or ("hien" in userContent)) 
          and (("gio" in userContent) or ("thoi gian" in userContent) or ("phut" in userContent) or ("giay" in userContent))):
        answer = "Hiện tại là " + str(time()[0]) + " giờ " + str(time()[1]) + " phút theo giờ Việt Nam."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))
          and (("âm" in userContent) or ("ta" in userContent))) or ((("may" in userContent) or ("nao" in userContent) or ("la" in userContent)) 
          and (("ngay" in userContent) or ("buoi" in userContent) or ("thang" in userContent) or ("nam" in userContent))
          and (("hien" in userContent) or ("nay" in userContent))
          and (("am" in userContent) or ("ta" in userContent))):
        answer = "Xin lỗi tôi không có kiến thức sử dụng lịch âm, xin lỗi vì sự bất tiện."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))) or ((("may" in userContent) or ("nao" in userContent) or ("la" in userContent)) 
          and (("ngay" in userContent) or ("buoi" in userContent) or ("thang" in userContent) or ("nam" in userContent))
          and (("hien" in userContent) or ("nay" in userContent))):
        answer = "Hôm nay là ngày " + str(time()[2]) + " tháng " + str(time()[3]) + " năm " + str(time()[4]) + "."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("thứ" in userContent) or (("ngày" in userContent) and ("tuần" in userContent)))
          and (("hiện" in userContent) or ("nay" in userContent))) or ((("may" in userContent) or ("bao" in userContent) or ("la" in userContent)) 
          and (("thu" in userContent) or (("ngay" in userContent) and ("tuan" in userContent)))
          and (("hien" in userContent) or ("nay" in userContent))):
        answer = gptService("ngày " + str(time()[2]) + " tháng " + str(time()[3]) + " năm " + str(time()[4]) + "là thứ mấy")
    elif (("bạn" in userContent) and (("tên" in userContent) or ("là" in userContent) or ("gì" in userContent))) or (("ban" in userContent) and (("ten" in userContent) or ("la" in userContent) or ("gi" in userContent))):
        answer = "Tôi là trợ lý ảo do nhóm 4 tạo ra, tôi tên là SmartHome"
      
    else:
        answer = gptService(userContent)

    return answer

def assistantModel_en(userContent):
    if userContent == "":
        answer = "Sorry, I didn't hear clearly"
    elif (("fan" in userContent) or ("light" in userContent)):
        if (("on" in userContent) and ("fan" in userContent) and ("light" in userContent)):
            answer = "I turned on the fan and lights."
        elif (("off" in userContent) and ("fan" in userContent) and ("light" in userContent)):
            answer = "I turned off the fan and lights."
        elif (("on" in userContent) and ("light" in userContent)):
            answer = "I turned on the light."
        elif (("off" in userContent) and ("light" in userContent)):
            answer = "I turned off the light."
        elif (("on" in userContent) and ("fan" in userContent)):
            answer = "I turned on the fan."
        elif (("off" in userContent) and ("fan" in userContent)):
            answer = "I turned off the fan."
        else:
            answer = "I can adjust the status of these two devices, can you say it more clearly."

    elif ("hello" in userContent) or ("hi" in userContent):
        answer = "Hello, I'm a smart home virtual assistant."
    elif ((("how many" in userContent) or ("how much" in userContent) or ("about" in userContent) or ("show" in userContent) or ("what" in userContent))
        and (("hours" in userContent) or ("time" in userContent) or ("minutes" in userContent) or ("seconds" in userContent))):
        answer = "The current time is " + str(time()[0]) + " hours " + str(time()[1]) + " minutes in Vietnam time."
    elif ((("which" in userContent) or ("which" in userContent) or ("is" in userContent))
        and (("day" in userContent) or ("session" in userContent) or ("month" in userContent) or ("year" in userContent))
        and (("now" in userContent) or ("now" in userContent))
        and (("negative" in userContent))):
        answer = "Sorry I don't have the knowledge to use the lunar calendar, sorry for the inconvenience."
    elif ((("which" in userContent) or ("which" in userContent) or ("is" in userContent))
        and (("day" in userContent) or ("session" in userContent) or ("month" in userContent) or ("year" in userContent))
        and (("now" in userContent) or ("now" in userContent))):
        answer = "Today is the day " + str(time()[2]) + " month " + str(time()[3]) + " year " + str(time()[4]) + "."
    elif ((("which" in userContent) or ("which" in userContent) or ("is" in userContent))
        and (("day" in userContent) or (("day" in userContent) and ("week" in userContent)))
        and (("now" in userContent) or ("now" in userContent))): 
        answer = gptService("day " + str(time()[2]) + "month" + str(time()[3]) + "year" + str(time()[4]) + "what day is it ")
    elif (("name" in userContent) and (("you" in userContent) or ("is" in userContent) or ("what" in userContent))):
        answer = "I am a virtual assistant created by group 4, my name is SmartHome."
    
    else:
        answer = gptService(userContent)

    return answer