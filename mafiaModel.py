"""
Characters:
- Townie (Innocent)
- Mafia
- Cop (Detective)
- Doctor
"""

# Class for Townie
class Townie(object):
	"""
	Welcome, [Player Name], you are a Vanilla Townie.

	Abilities:
	- Your weapon is your vote, you have no night actions.

	Win Condition:
	- You win when all threats to the town have been eliminated.
	"""

	name = ""
	slackId = ""
	slackChannel = ""
	role = 'Townie'
	voteToken = True
	isAlive = True

	def __init__(self, name, slackId, slackChannel):
		self.name = name
		self.slackId = slackId
		self.slackChannel = slackChannel

	def vote():
		print "I VOTE!"

# Class for Mafia
class MafiaGoon(object):
	"""
	Welcome, [Player Name]. You are a Mafia Goon, along with your partner, [Partner Name].

	Abilities:
	- Factional Communication: During the night phase you may talk with your partner here
	- Factional kill: Each night phase, one of you or your partner may perform the factional kill.

	Win Condition:
	- You win when all members of the town have been eliminated or nothing can prevent this from occuring.
	"""

	name = ""
	slackId = ""
	slackChannel = ""
	role = 'Mafia Goon'
	voteToken = True
	isAlive = True

	def __init__(self, name, slackId, slackChannel):
		self.name = name
		self.slackId = slackId
		self.slackChannel = slackChannel

	def kill():
		print "KILL HIM!"

# Class for Cop
"""
Later Development... coming soon!
"""

# Class for Doctor
"""
Later Development... coming soon!
"""

