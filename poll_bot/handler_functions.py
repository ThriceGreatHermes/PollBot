import sys


def handle_hello(slack_client, msg_obj) -> None:
    channel = msg_obj.get('channel')
    slack_client.api_call('chat.postMessage', channel=channel, text="Hiya!")


def handle_go_away(slack_client, msg_obj) -> None:
    channel = msg_obj.get('channel')
    slack_client.api_call('chat.postMessage', channel=channel, text="Okay...")
    sys.exit(0)
