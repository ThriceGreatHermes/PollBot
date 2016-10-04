import argparse
from slackclient import SlackClient
from time import sleep
from handler import HandlerManager, KeywordHandler
from handler_functions import handle_hello, handle_go_away


BOT_NAME = "pollbot"
DEFAULT_POLLING_PERIOD = .5


def get_bot_id(slack: SlackClient) -> str:
    all_users = slack.api_call("users.list")
    if all_users.get('ok'):
        users = all_users.get('members')
        for user in users:
            name = user.get('name', '')
            if name == BOT_NAME:
                return user.get('id')


def construct_handler(slack_client: SlackClient) -> HandlerManager:
    handler_manager = HandlerManager(slack_client)
    hello_handler = KeywordHandler('hi', handle_hello)
    go_away_handler = KeywordHandler('go away', handle_go_away)

    handler_manager.add_handler(hello_handler)
    handler_manager.add_handler(go_away_handler)
    return handler_manager


def slack_bot(token: str) -> None:
    slack = SlackClient(token)
    my_id = get_bot_id(slack)
    handler = construct_handler(slack)

    if slack.rtm_connect():
        while True:
            msg = slack.rtm_read()
            if msg:
                for event in msg:
                    if event['type'] == 'message':
                        text = event['text']
                        if '@{}'.format(my_id) in text:
                            handler.on_message(event)
            sleep(DEFAULT_POLLING_PERIOD)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, required=True, help="Slack token")
    args = parser.parse_args()

    slack_bot(args.token)
