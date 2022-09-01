import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
saturday_msg_text = "<@U03L1REEJDC> <@U03L8C3RZ0B> <@U03L27ZH2J2> This is a reminder for the meeting."
msg_text = "<@U03L8C3RZ0B> <@U03L27ZH2J2> This is a reminder for the meeting."

client = slack.WebClient(token=os.environ["API_TOKEN"])
last_sent_message_day = -1
last_sent_message_minute = -1

while True:
    now = datetime.datetime.now()

    if now.day != last_sent_message_day and now.hour == 19 and now.minute == 15:
        last_sent_message_day = now.day
        if datetime.datetime.today().weekday() == 5: # if today is Saturday
            client.chat_postMessage(channel="#announcements", text=saturday_msg_text)
        else if datetime.datetime.today().weekday() == 6: # everyone deserves a break on Sundays
            pass
        else:
            client.chat_postMessage(channel="#announcements", text=msg_text)

    if now.minute != last_sent_message_minute and now.minute % 5 == 0:
        print(now)
        last_sent_message_minute = now.minute
