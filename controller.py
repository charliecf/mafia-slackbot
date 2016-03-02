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

# Initialize Game
def startGame(newGamePlayersName, gameSetup):
	## Assign Roles
	## Game Mode
	players = {}
	gameSetupCounter = 0
	for player in newGamePlayersName:
	    players[player] = makePlayer(gameSetup[gameSetupCounter], 
	        player, "slackId", "slackChannel")
	    gameSetupCounter += 1

	for player in players:
	    selfIdentification(players[player])

	## Explain Rules
	gameRuleIntro = """
	Explaining rules...
	"""
	print gameRuleIntro
	return players # so that the object dictionary of players in game is created

def selfIdentification(player):
	print "%s is a %s" % (player.name, player.role)

# ----------------------------------------------
# ---------- controller functions end ----------
# ----------------------------------------------

print "-----------------------------------------"

# Testing
# 7 Dummy Players
# This is strictly temporary
newGamePlayersName = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7']

gameSetup = ["MafiaGoon", "MafiaGoon", "Townie", "Townie", "Townie", "Townie", "Townie"]
gameSetup = shuffleRoles(gameSetup)
print gameSetup

# Exit game if not enough players or too many
if len(newGamePlayersName) != 7:
	print "Too many players or too few!"
	exit()

players = startGame(newGamePlayersName, gameSetup)

for player in players:
	print players[player].isAlive

# breakLine = raw_input("> ")

# Initialize Game
# Start Game
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
		if "vote lynch:" in vote:
			# Identify who it is:
			print vote[0]
			print vote[1]
			playerName = raw_input("Who are you? > ")

			# If voted already, change vote
			# If not voted yet, new vote and put in dictionary
			voteLynch = vote.replace("vote lynch: ", "")
			playerVotes[playerName] = voteLynch
			print playerVotes
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