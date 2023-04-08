from flask import Flask, render_template, request, redirect, url_for
import openai
import requests
import os
from config import openapi_key
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = "Secretsecret"

api_endpoint = "https://api.openai.com/v1/completions"


api_key = openapi_key()



class Questions(FlaskForm):
    ask = StringField('ask', validators=[DataRequired()])
   

my_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}



@app.route('/', methods=['GET', 'POST'] )
def index():
    form= Questions()
    request_data = {
        "model": "text-davinci-003",
        "prompt": form.ask.data,
        "max_tokens": 100,
        "temperature": 0.7,     
        
        
        }
    if form.validate_on_submit():
        
         response = requests.post(api_endpoint, headers=my_headers, json=request_data)

    if response.status_code== 200:
        print(response.json())

    else:
        print(f" Falied {response.status_code}")

    answers=response.json()
    for answer in answers['choices']:
        print(answer['text'])
        return render_template('index.html',answer=answer['text'], form=form)


if __name__ == '__main__':
    app.run(debug=True)
