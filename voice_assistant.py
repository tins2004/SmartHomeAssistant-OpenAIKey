import asyncio
import json
import websockets
import enchant

from assistant_service import assistantModel_vi, assistantModel_en


checkEn = enchant.Dict("en_US")

def checkEnService(content) -> str:
    temp = content.split()
    count_vi = 0
    count_en = 0
    for i in temp:
        if checkEn.check(i):
            count_en += 1
        else:
            count_vi += 1
    
    if  count_vi < count_en:
        language = "en"
    else:
        language = "vi"
    
    return language

def assistant(userContent):
    language = checkEnService(userContent)

    if language == "vi":
        userContent = userContent.lower()
        answer = assistantModel_vi(userContent)
        return answer
        
    elif language == "en":
        userContent = userContent.lower()
        answer = assistantModel_en(userContent)
        return answer

async def webSocketService(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        text = data["text"]
        # print(text)
        
        answerMessage = assistant(text)
        language = checkEnService(answerMessage)

        response_data = {"status": "success", "message": [answerMessage, language]}

        await websocket.send(json.dumps(response_data))



asyncio.get_event_loop().run_until_complete(
    websockets.serve(webSocketService, "192.168.0.4", 8080)
)


asyncio.get_event_loop().run_forever()