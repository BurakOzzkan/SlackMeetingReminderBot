import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
msg_text = "<@U03NG0TR2E9> <@U03L1REEJDC> <@U03L8C3RZ0B> <@U03L27ZH2J2> <@U03LY67SPR6> Herkesi toplantıya bekliyoruz."

client = slack.WebClient(token=os.environ["API_TOKEN"])
last_sent_message_day = 12

while True:
    now = datetime.datetime.now()

    if(now.day != last_sent_message_day and now.hour == 16 and now.minute == 30):
        last_sent_message_day = now.day
        client.chat_postMessage(channel="#announcements", text=msg_text)
