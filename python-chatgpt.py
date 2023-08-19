import requests
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")
args = parser.parse_args()


api_endpoint='https://api.openai.com/v1/completions'
open_api_secret=os.getenv("OPENAI_API_KEY")
headers={
    'Content-Type':'application/json',
    'Authorization':'Bearer '+open_api_secret
}

data={
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 10,
    "temperature": 0.2
  }
response=requests.post(api_endpoint, headers=headers,json=data)
if response.status_code==200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f'Request failed with:{str(response.status_code)} and {response.content}')