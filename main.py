#importing libs---------------------------------------------------------------------------
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
import json
#to read .env-----------------------------------------------------------------------------
from pathlib import Path 
from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initializes your app with your bot token and socket mode handler------------------------
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# Match any message-----------------------------------------------------------------------
@app.message(re.compile(r".*"))  
def message_any(message, say, client):
    # Get the user ID
    user_id = message['user']
   
    # Retrieve the user's information
    user_info = client.users_info(user=user_id)
    
    # Extract the user's email
    email = user_info['user']['profile'].get('email')

    # Send a response message with the user's email
    if email:
        #code to validate permissions and roles
            #say(f"Your email is: {email}", channel=user_id)

        messageFromUser = message["text"].split() 
        print(f"Message from User:  {messageFromUser}")
        print(len(messageFromUser))

        #CA2 API call to handle "Company name" and return general info      #company_name  
        companyFormat = r"^#[a-zA-Z0-9_]+$"
        #CA2 API call to handle "Company name" and return general info with Email  #company_name  +email
        companyEmailFormat = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b" 
                            
       
        if len(messageFromUser)<3 and re.match(companyFormat, messageFromUser[1]):#Returns info to slack
            #say(f"Your asking for company{message} info")
            print(f"Your asking for  {messageFromUser[1]} ")
        elif (len(messageFromUser)==3) and (re.match(companyFormat, messageFromUser[1])) and  ("mailto:" in  messageFromUser[2]):#Retursn Info to Slack and send info Users Email 

            #say(f"Your asking for company{message} info")
            print(f"Your asking for  {messageFromUser[1]} info and send it to {email} account")
        else:
            #say(f"Sorry, I can not understand that instruction")
            print("Sorry, I can not understand that instruction")
        
           

        
    else:
        say("Sorry, I couldn't retrieve your email to validate your permissions.")






# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
