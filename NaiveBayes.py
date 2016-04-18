import warnings
import numpy as np
from sklearn.naive_bayes import GaussianNB
from pymongo import MongoClient

client = MongoClient()
db = client['vocabulary-builder']
words = db['words']
users = db['users']
result = db['train-result']

def rightOrWrong(number):
	"""
	If number <= zero, returns -1
	Else returns +1
	"""
	if number <= 0:
		return -1
	else:
		return 1

def setWordClass(probList):
	"""
	Calculates and returns the class of the word
	probList: List, probabilities corresponding to class -1 and 1 respectively
	[P(Class -1), P(Class +1)]
	returns the class to which the word belongs
	"""
	if probList[0] >= probList[1]:
		return -abs(round(probList[0], 4))
	else:
		return abs(round(probList[1], 4))

def getClassList(username):
	userAtt = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
	return map(lambda x : rightOrWrong(x['wordClass']), userAtt.values())

def getFeatures(username):
	userAtt = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
	features = []
	for key in userAtt.keys():
		feat = words.posts.find_one({'word' : key}, {'id' : 1,
													'points' : 1,
													'diff' : 1,
													'_id' : 0})
		# print map(lambda x : (x['id'], x['points'], x['diff']) ,feat)
		feat = (feat['id'], feat['points'], feat['diff'])
		features.append(feat)
	return features

def trainData(username):
	"""
	Trains the data based on the users performance so far
	Returns a trained Gaussian Naive Bayes model and updates result collection
	"""
	X = getFeatures(username)
	Y = getClassList(username)
	
	trainX = np.array(X)
	trainY = np.array(Y)

	gnb = GaussianNB()
	gnb.fit(trainX, trainY)
	print "Score with Naive Bayes: ", gnb.score(trainX, trainY)

	testData = words.posts.find({}, {'id' : 1,
									'points' : 1,
									'diff' : 1,
									'_id' : 0})
	testData = map(lambda x : (x['id'], x['points'], x['diff']), testData)

	with warnings.catch_warnings():
		warnings.simplefilter('ignore')
		for data in testData:
			testWord = words.posts.find_one({'id' : data[0]}, {'word' : 1, '_id' : 0})['word']
			wordClass = setWordClass(list(gnb.predict_proba(data))[0])
			classWord = result.posts.update({'username' : username}, {'$set' : {testWord : wordClass}}, upsert = True)