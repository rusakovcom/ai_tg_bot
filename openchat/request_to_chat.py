# Openchat model by https://serverspace.ru/services/serverspace-gpt-api/
# Run script as: 
# python request_to_chat.py "How to install Docker on MacOS"

import requests
import json
import sys
import os
from dotenv import load_dotenv



# Load environment variables from .env file and accessing environment variables
load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")



# Check if an argument is passed,
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = "Hello"  # Default message



# Request to endpoint with user_input for getting response
url = "https://gpt.serverspace.ru/v1/chat/completions"
payload = {
  "model": "openchat-3.5-0106",
  "max_tokens": 1024,
  "top_p": 0.9,
  "temperature": 0.5,
  "messages": [
    {
      "role": "user",
      "content": user_input # INPUT to chat
    }
  ]
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Bearer {bearer_token}"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))



# Checking for success request and gitting content from response
if response.status_code == 200:
    # print(response.json()) # full OUTPUT    
    content = response.json()['choices'][0]['message']['content']
    print(content)

else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
