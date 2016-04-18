from pymongo import MongoClient
client = MongoClient()

usersDB = client['vocabulary-builder']
users = usersDB['users']
result = usersDB['train-result']

def createUser(username, name, userType, secret):
	"""
	Creates new user if username is not already taken
	"""
	if users.posts.find_one({'username' : username}):
		print "Sorry! This username has already been taken"
		newUser = None
	else:
		user = {'username' : username,
				'name' : name,
				'userType' : userType,
				'secret' : secret
		}
		userResult = {'username' : username}
		newUser = users.posts.insert_one(user)
		newUser = result.posts.insert_one(userResult)
		print "User " + str(username) + " successfully created!"

def deleteUser(username):
	"""
	Deletes user if user is present
	"""
	if users.posts.find_one({'username' : username}):
		delUser = users.posts.delete_one({'username' : username})
		delUser = result.posts.delete_one({'username' : username})
		print 'User ' + str(username) + ' successfully deleted!'
	else:
		print "No such user!"
		delUser = None

def verifyUser(username):
	"""
	Verifies the user.
	Prints whether the user exists or not
	"""
	if users.posts.find_one({'username' : username}):
		print "User already exists"
	else:
		print "This username is available"

def updateAttempts(username, word, answer):
	"""
	Updates the appropriate word dictionary and it's corresponding attributes
	answer = 1 means correct
	answer = -1 means wrong
	"""
	myID = {'username' : username}
	totalAttempts = word + '.totalAttempts'
	correctAttempts = word + '.correctAttempts'
	wrongAttempts = word + '.wrongAttempts'
	wordClass = word + '.wordClass'
	if answer == 1:
		update = users.posts.update(myID, {'$inc' : {totalAttempts : 1,
													correctAttempts : 1,
													wrongAttempts : 0,
													wordClass : 1}})
	elif answer == -1:
		update = users.posts.update(myID, {'$inc' : {totalAttempts : 1,
													correctAttempts : 0,
													wrongAttempts : 1,
													wordClass : -1}})
	else:
		print 'Invalid input for parameter : answer'