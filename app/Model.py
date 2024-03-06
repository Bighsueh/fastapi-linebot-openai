from pydantic import BaseModel
import requests
import app.Chat as Chat

class ChatInfo(BaseModel):
    temperature: float = 0.7
    max_tokens: int = 800
    top_p : float = 0.95
    purpose :str = "none"
    api_url : str
    prompt_text : Chat.ChatlogFormat

def callGPT(chat_info : ChatInfo):
    target_url = chat_info.api_url
    
    request_body = {
            "engine": "gpt-35-turbo-16k",
            "temperature": chat_info.temperature,
            "max_tokens": chat_info.max_tokens,
            "top_p": chat_info.top_p,
            "top_k": 5,
            "roles": chat_info.prompt_text,
            "frequency_penalty": 0,
            "repetition_penalty": 1.03,
            "presence_penalty": 0,
            "stop": "",
            "past_messages": 10,
            "purpose": chat_info.purpose
        }

    response = requests.post(target_url, json=request_body)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print("request error:", response.status_code)
        return response.content
