from openai import OpenAI
import datetime

client = OpenAI(api_key="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")

def gptService(userContent):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a useful virtual assistant in the smart home."},
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

def assistantModel(userContent):
    if userContent == "":
        answer = "Xin lỗi, tôi không nghe rõ"
    elif (("nhóm 4" in userContent) or ("nhóm bốn" in userContent)) :
        answer = "Tôi vẫn đang hoạt động."
    elif "xin chào" in userContent:   
        answer = "Xin chào, tôi là trợ lý ảo nhà thông minh."
    elif ((("mấy" in userContent) or ("bao nhiêu" in userContent)) and ("giờ" in userContent)     
        or (("thời gian" in userContent) and ("hiện tại" in userContent))):
        answer = "Bây giờ là " + str(time()[0]) + " giờ " + str(time()[1]) + " phút."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))
          and (("âm" in userContent) or ("ta" in userContent))):
        answer = "Xin lỗi tôi không có kiến thức sử dụng lịch âm, xin lỗi vì sự bất tiện."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("ngày" in userContent) or ("buổi" in userContent) or ("tháng" in userContent) or ("năm" in userContent))
          and (("hiện" in userContent) or ("nay" in userContent))):
        answer = "Hôm nay là ngày " + str(time()[2]) + " tháng " + str(time()[3]) + " năm " + str(time()[4]) + "."
    elif ((("mấy" in userContent) or ("nào" in userContent) or ("là" in userContent)) 
          and (("thứ" in userContent) or (("ngày" in userContent) and ("tuần" in userContent)))
          and (("hiện" in userContent) or ("nay" in userContent))):
        answer = gptService("ngày " + str(time()[2]) + " tháng " + str(time()[3]) + " năm " + str(time()[4]) + "là thứ mấy")
    elif ("bạn" in userContent) and (("tên" in userContent) or ("là" in userContent) or ("gì" in userContent)):
        answer = "Tôi là trợ lý ảo do nhóm 4 tạo ra tên là BÁO."
    elif ("quạt" in userContent) or ("đèn" in userContent):
        if ("bật" in userContent) and ("quạt" in userContent) and ("đèn" in userContent):
            answer = "Tôi đã bật quạt và đèn."
            statusLightAndFan[0] = 1
            statusLightAndFan[1] = 1
        elif ("bật" in userContent) and ("quạt" in userContent) and ("đèn" in userContent):
            answer = "Tôi đã tắt quạt và đèn."
            statusLightAndFan[0] = 0
            statusLightAndFan[1] = 0
        elif ("bật" in userContent) and ("đèn" in userContent):
            answer = "Tôi đã bật đèn."
            statusLightAndFan[0] = 1
        elif ("tắt" in userContent) and ("đèn" in userContent):
            answer = "Tôi đã tắt đèn."
            statusLightAndFan[0] = 0
        elif ("bật" in userContent) and ("quạt" in userContent):
            answer = "Tôi đã bật quạt."
            statusLightAndFan[1] = 1
        elif ("tắt" in userContent) and ("quạt" in userContent):
            answer = "Tôi đã tắt quạt."
            statusLightAndFan[1] = 0
        else:
            answer = "Tôi có thể điều chỉnh trạng thái hai thiết bị này, bạn có thể nói rõ ràng hơn."
        
        print(statusLightAndFan)
    elif ("tạm biệt" in userContent):
        answer = "Tạm biệt và hẹn gặp lại."

    else:
        answer = gptService(userContent)

    return answer