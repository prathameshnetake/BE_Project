import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pymongo import MongoClient
client = MongoClient()

usersDB = client['vocabulary-builder']
users = usersDB['users']
result = usersDB['train-result']

def wordCloudTotal(username):
	"""
	Generates a word cloud based on the total attempts for a word
	"""
	userWordTotal = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
	userWordTotal = map(lambda x : (x, userWordTotal[x]['totalAttempts']), userWordTotal)
	wc = WordCloud().fit_words(userWordTotal)
	plt.imshow(wc)
	plt.axis("off")
	plt.show()

def wordCloudCorrect(username):
	"""
	Generates a word cloud based on the total attempts for a word
	"""
	userWordCorrect = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
	userWordCorrect = map(lambda x : (x, userWordCorrect[x]['correctAttempts']), userWordCorrect)
	wc = WordCloud().fit_words(userWordCorrect)
	plt.imshow(wc)
	plt.axis("off")
	plt.show()

def wordCloudWrong(username):
	"""
	Generates a word cloud based on the total attempts for a word
	"""
	userWordWrong = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
	userWordWrong = map(lambda x : (x, userWordWrong[x]['wrongAttempts']), userWordWrong)
	wc = WordCloud().fit_words(userWordWrong)
	plt.imshow(wc)
	plt.axis("off")
	plt.show()