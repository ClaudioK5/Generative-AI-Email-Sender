import sys
import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
sys.path.append(os.path.abspath('backend'))
from prompts import create_prompt

#use this code down below when you will insert your own openai api key into the apikey.env file
#base_dir = os.getcwd()
#env_path = os.path.join(base_dir, 'config', 'apikey.env')
#load_dotenv(dotenv_path=env_path)
#api_key  = os.getenv("OPENAI_API_KEY")
#open.api_key = api_key

openai.api_key = "insert your openai api key here"

user_input = input('enter your prompt')

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate(user_input):

    
    #this piece of code will replace the hard-coded from python terminal "user_input = input('enter your prompt')"
    #data = request.get_json()
    #user_input = data.get('input')

    prompt = create_prompt(user_input)

    response = openai.chat.completions.create(model = "gpt-3.5-turbo",
                     messages = [ {'role': 'user', 'content': prompt }],
                     max_tokens = 150)

    ai_output = response.choices[0].message.content.strip()

    return ai_output

ai_output = generate(user_input)

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'bot email'
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('bot email','app password of the bot email')
        smtp.send_message(msg)

colleagues = ['example@gmail','example2@gmail','example3@gmail']

subject = "insert the subject of the message"

for email in colleagues:
    send_email(email, subject, ai_output)
    print(f"Email sent to {email} successfully!")

if __name__ == '__main__':
    app.run(debug=True)