import requests
import random
import json
import settings

with open("quotes.txt") as f:
    all_messages = f.readlines()

with open("used_quotes.txt") as f:
    used_messages = f.readlines()

available_messages = list(set(all_messages) - set(used_messages))

if len(available_messages) == 0:
    available_messages = all_messages
message = random.choice(available_messages)
used_messages.append(message)

with open("used_quotes.txt", "w+") as f:
    f.writelines(used_messages)

payload = {
    "text": message,
    "username": "Biden Facts"
}
result = requests.post(settings.url, data=json.dumps(payload))
