import mafiaModel, slackView

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

# Initialize Game
def startGame():
	## Assign Roles

	## Explain Rules
	
	return None

# DayTime Object
def dayTime():
	## Voting

	## Communication
	return None	

# NightTime Object
def nightTime():
	## Mafia Killing

	## Communication between Mafia
	return None


# ----------------------------------------------
# ---------- controller functions end ----------
# ----------------------------------------------

# Testing
# 7 Dummy Players
# This is strictly temporary
newGamePlayersName = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7']


# Exit game if not enough players or too many
if len(newGamePlayersName) != 7:
	print "Too many players or too few!"
	exit()

