import json
import requests

def get_hostname():
    return "ASG-TEST"

def slack_message(event, exc):
    'Format message for slack'
    return ('Test Message exc: {}\n\n'
            'Test Message event: {}').format(exc, event)

def send_message_in_slack(event, exc):
    "Inform by slack we couldn't failed to publish event or metric to signalfx"
    requests.post('https://hooks.slack.com/services/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',
                  data=json.dumps({"text": slack_message(event, exc),
                                   "channel": "asg_test_pvt2",
                                   "username": get_hostname()}))


send_message_in_slack("EVENT-ABC", "EXC")

print "ok"