import requests

API_KEY = "https://api.telegram.org/bot5457629160:AAFaUtRgOoikY8xBmQCTUrSK5bBmp3-FZC8"

response = requests.get(API_KEY + "/getUpdates?offset=-1").json()

message = response["result"][0]["message"]

chat_id = message["from"]["id"]

text = message["text"]

print(response)
print(message)
print(chat_id)
print(text)

send_message = requests.get(API_KEY + f"/sendMessage?chat_id={chat_id}&text={text}")