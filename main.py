#importing libs---------------------------------------------------------------------------
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
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
    mx =message
    # Retrieve the user's information
    user_info = client.users_info(user=user_id)
    
    # Extract the user's email
    email = user_info['user']['profile'].get('email')

    # Send a response message with the user's email
    if email:
        #code to validate permissions and roles
        say(f"Your email is: {email}")
    else:
        say("Sorry, I couldn't retrieve your email to validate your permissions.")






# Start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    