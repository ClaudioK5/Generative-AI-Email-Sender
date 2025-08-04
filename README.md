# Generative-AI-Email-Sender

This pipeline automates the process of generating custom emails using OpenAI's GPT API and sends them to multiple recipients via SMTP. 

**Key Features**

- Fast and light weight (around 50 lines of code);
- Easily scalable to accept JSON input from external interfaces;

**Setup Instructions**
  
- Bot Email: create a google email that will have the only objective of sending emails. Once that is done, create a google app password for the email sending messages. Please notice  that the normal password won't work for this pipeline. You are going to need specifically an app password;
- API Key: insert your OpenAI API key in the apikey.env file;
- Recipients: add target emails in the colleagues list inside main.py;
- For UI integration: replace the terminal input with a JSON request object (part of the code is already in place)
