import os
import time
import re
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# bot's user ID in slack
scroobot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading after the bot starts
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|]WU].+?>(.*)"

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Scroobot is working!")
        # Read bot's suer id
        scroobot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
        else:
            print("Connection failed.")