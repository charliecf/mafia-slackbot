import time
import pprint
import json
from slackclient import SlackClient

token = "xoxb-22371870822-R4NMrSgKKyldo4xJj7nQNM4F" # Random Projects -- will need to change in the future
sc = SlackClient(token)

groupChannel = "C0NCQ4K4K"

def compileUserListDic():
	userListDic = {}
	for user in usersList:
		name = user['name']
		slackId = user['id']
		for im in imList:
			if im['user'] == slackId:
				channelId = im['id']
		userListDic[slackId] = [name, slackId, channelId]

	return userListDic

def postMessage(channel, message):
	print sc.api_call("chat.postMessage", channel=channel, text=message, as_user="true")

def getUserInput(channel):
	sc.rtm_connect()
	while True:
	    new_evts = sc.rtm_read()
	    # print new_evts
	    for evt in new_evts:
	        print(evt)
	        if "type" in evt:
	            if evt["type"] == "message" and "text" in evt and evt["channel"] == channel:
	                message = evt["text"]
	                return message
	    time.sleep(1)

def getUserInputTimeout(channel, timeout):
	"""
	channel = Slack Channel ID
	timeout = int in seconds

	This is used for challenges and optional inputs where input times out 
	after a certain limit. 
	"""
	timeoutTimer = 0
	sc.rtm_connect()
	while timeoutTimer < int(timeout):
	    new_evts = sc.rtm_read()
	    # print new_evts
	    for evt in new_evts:
	        print(evt)
	        if "type" in evt:
	            if evt["type"] == "message" and "text" in evt and evt["channel"] == channel:
	                message = evt["text"]
	                user = evt["user"]
	                return message, user
	    time.sleep(1)
	    timeoutTimer += 1
	return None, None
