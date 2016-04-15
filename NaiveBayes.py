import warnings
import numpy as np
import random
from sklearn.naive_bayes import GaussianNB
from pymongo import MongoClient

def loadWords():
	wordsDB = open("Final Words DB", 'r')
	rawDB = []
	for line in wordsDB:
		rawDB.append(line.strip().split('\t'))
	wordsDB.close()
	return rawDB

# wordsData = loadWords()

client = MongoClient()
db = client['vocabulary-builder']
wordsCollection = db['words']

print str(db.posts.count()) + " words loaded"
one = list(db.posts.find({} , {'id' : 1, 'points' : 1, 'diff' : 1}))
# print type(one), len(one)
# print one[0], one[1]

feat = map(lambda x : (x['id'], int(x['points']), int(x['diff'])), one)
# print type(feat)
# print feat[0]

X = random.sample(feat, 20)
Y = []
for x in X:
	print db.posts.find_one({'id' : x[0]}, {'word' : 1})['word'],
	Y.append(int(raw_input("1/-1? ")))

print Y

trainX = np.array(X)
trainY = np.array(Y)

gnb = GaussianNB()
gnb.fit(trainX, trainY)
print "Score with Naive Bayes: ", gnb.score(trainX, trainY)

testData = feat[4700 : ]
with warnings.catch_warnings():
	warnings.simplefilter('ignore')
	for data in testData:
		print gnb.predict_proba(data)