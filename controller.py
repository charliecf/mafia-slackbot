import mafiaModel, slackView

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

def selfIdentification(player):
	print "%s is a %s" % (player.name, player.role)

# ----------------------------------------------
# ---------- controller functions end ----------
# ----------------------------------------------

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

startGame(newGamePlayersName, gameSetup)

# breakLine = raw_input("> ")

# Initialize Game
day = "Day"
# Start Game
while True:	
	## Day
	print "Day"
	vote = raw_input("How do you vote? >")

	## Night
	print "Night"

