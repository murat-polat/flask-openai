from flask import Flask, render_template, request, redirect, url_for
import openai
import requests
import os
from config import openapi_key


app = Flask(__name__)



api_endpoint = "https://api.openai.com/v1/completions"


api_key = openapi_key()


   

my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
request_data = {
    "model": "text-davinci-003",
    "prompt": " what is a pigeon ?",
    "max_tokens": 100,
    "temperature": 0.7,     
     
     
      }


@app.route('/')
def index():
    response = requests.post(api_endpoint, headers=my_headers, json=request_data)

    if response.status_code== 200:
        print(response.json())

    else:
        print(f" Falied {response.status_code}")

    answers=response.json()
    for answer in answers['choices']:
        print(answer['text'])
        return render_template('index.html',answer=answer['text'])


if __name__ == '__main__':
    app.run(debug=True)
