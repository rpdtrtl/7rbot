import os
import sys
import requests
import json
from dotenv import load_dotenv

load_dotenv()

original_stdout = sys.stdout

messages = []
channelid = os.getenv('CHANNEL_ID')
def retrieve_messages(channelid):
    headers = {
        'authorization': os.getenv(str('AUTH_TOKEN'))
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    with open("messages.txt", "w", encoding="utf-8") as f:
        for value in jsonn:
            sys.stdout = f
            print(value,'\n')
            sys.stdout = original_stdout

retrieve_messages(channelid)