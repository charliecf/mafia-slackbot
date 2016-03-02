import mafiaModel
from slackView import *

import random
"""
C9 Variation
http://wiki.mafiascum.net/index.php?title=C9

Setup:
2 Mafia Goons, 	5 Townie
"""

# ---------- controller functions start ----------
"""
These functions bridge the gap between Model and View
Functions in these category should require both player input as well as 
changing backend data
"""

def shuffleRoles(roles):
    shuffledRoles = []
    for i in range(len(roles)):
        element = random.choice(roles)
        roles.remove(element)
        shuffledRoles.append(element)
    return shuffledRoles

def makePlayer(role, name, slackId, slackChannel):
	if role == "MafiaGoon":
		player = mafiaModel.MafiaGoon(name, slackId, slackChannel)
	if role == "Townie":
		player = mafiaModel.Townie(name, slackId, slackChannel)

	return player

def selfIdentification(player):
	print "%s is a %s" % (player.name, player.role)

def getPlayerFromSlackId(players, slackId):
    for player in players:
        if players[player].slackId == slackId:
            return players[player]
    return None

# ----------------------------------------------
# ---------- controller functions end ----------
# ----------------------------------------------

postMessage(groupChannel, "-----------------------------------------")
postMessage(groupChannel, "Welcome kids...")
postMessage(groupChannel, "I'm the don :ok_hand:, so follow my instructions to the tee, cause I ain't repeating myself...")
print "-----------------------------------------"
# How many players?
userListDic = compileUserListDic()

postMessage(groupChannel, "Who's in? Type 'join game'")
newGamePlayersId = []
newGamePlayersName = []
timeoutTimer = 0
sc.rtm_connect()
while timeoutTimer < 30:
    new_evts = sc.rtm_read()
    for evt in new_evts:
        print(evt)
        if "type" in evt:
            if evt["type"] == "message" and "text" in evt and evt["channel"] == groupChannel:
                message = evt["text"]
                user = evt["user"]
                if message == 'join game':                
                    newGamePlayersId.append(user)
                    postMessage(groupChannel, "%s successfully joined" % userListDic[user][0])
                    newGamePlayersName.append(userListDic[user][0])
                    print sc.api_call("im.open", user=user)
                print newGamePlayersId
    time.sleep(1)
    timeoutTimer += 1

print newGamePlayersName
print newGamePlayersId

# Exit game if not enough players or too many
if len(newGamePlayersId) < 2: # Change this to != 7 later
    postMessage(groupChannel, "Too many players or too few!")
    exit()

postMessage(groupChannel, "Starting a new game with: %s" % newGamePlayersName)

# C9 - Proper Setup
# gameSetup = ["MafiaGoon", "MafiaGoon", "Townie", "Townie", "Townie", "Townie", "Townie"]
gameSetup = ["MafiaGoon", "MafiaGoon", "Townie", "Townie", "Townie", "Townie", "Townie"]
gameSetup = shuffleRoles(gameSetup)
print gameSetup

print userListDic
players = {}
gameSetupCounter = 0
for player in newGamePlayersId:
    players[userListDic[player][0]] = makePlayer(gameSetup[gameSetupCounter], 
        userListDic[player][0], player, userListDic[player][2])
    gameSetupCounter += 1

# name, slackId, slackChannel (DM)

for player in players:
    selfIdentification(players[player])

## Explain Rules
gameRuleIntro = """
Explaining rules...
"""
print gameRuleIntro
postMessage(groupChannel, gameRuleIntro)
print players

for player in players:
	print players[player].isAlive

# breakLine = raw_input("> ")

# Initialize Game
# Begin Game
print "-----------------------------------------"
postMessage(groupChannel, "-----------------------------------------")
while True:	
	## Day
	postMessage(groupChannel, "Day Time")
	playerVotes = {}
	print playerVotes
	postMessage(groupChannel, "How do you vote?")
	while True:
		# Check and print players who has not voted yet
		vote = getUserInput(groupChannel)
		print vote[0]
		print vote[1]
		if "vote lynch:" in vote[0]:
			# Identify who it is:
			voteUser = getPlayerFromSlackId(players, vote[1])

			# If voted already, change vote
			# If not voted yet, new vote and put in dictionary
			voteLynch = vote[0].replace("vote lynch: ", "")
			print voteLynch

			playerVotes[voteUser.name] = voteLynch
			print playerVotes
			postMessage(groupChannel, playerVotes)
			playerNamefsd = raw_input("Who are you? > ")

			if len(playerVotes) == 3: # change to 7 later
				print "voting complete!"
				break

	## Night
	print "Night"
	print "Night time, only Mafia Goons may communicate to each another"
	# Enable communication between Mafia Goons
	# Allow Mafia Goon to Kill
	while True:
		vote = raw_input("How do you kill... Mr. Mafia? > ")
		if "vote kill:" in vote:
			voteKill = vote.replace("vote kill: ", "")
			print "Are you sure to kill", voteKill, "?"
			break

	print "Check Winning Condition"
	for player in players:
		print players[player].isAlive