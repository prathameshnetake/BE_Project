import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pymongo import MongoClient
client = MongoClient()

usersDB = client['vocabulary-builder']
users = usersDB['users']
result = usersDB['train-result']
words = usersDB['words']

def wordCloud(username, parameter):
	"""
	Generates a word cloud based on the parameter for specified username
	parameter : total, correct, wrong
	"""
	userWord = users.posts.find_one({'username' : username}, {'username' : 0, 'name' : 0, 'userType' : 0, 'secret' : 0, '_id' : 0})
	userWord = map(lambda x : (x, userWord[x][parameter + 'Attempts']), userWord)
	wc = WordCloud().fit_words(userWord)
	plt.imshow(wc)
	plt.axis("off")
	plt.show()


def pieChart(username, parameter):
	"""
	Generates a pie chart based on the parameter for specified username
	parameter : total, correct, wrong
	"""
	userWord = users.posts.find_one({'username' : username}, {'username' : 0, 'name' : 0, 'userType' : 0, 'secret' : 0, '_id' : 0})
	userWord = map(lambda x : (len(x), userWord[x][parameter + 'Attempts']), userWord)

	le4, le7, le10, g10 = 0, 0, 0, 0
	for l, num in userWord:
		if l <= 4:
			le4 += num
		elif 4 < l <= 7:
			le7 += num
		elif 7 < l <= 10:
			le10 += num
		else:
			g10 += num

	total = le4 + le7 + le10 + g10
	le4 = round((le4 / float(total)) * 100, 2)
	le7 = round((le7 / float(total)) * 100, 2)
	le10 = round((le10 / float(total)) * 100, 2)
	g10 = round((g10/ float(total)) * 100, 2)

	plt.figure()
	labels = 'Length <= 4', '4 < Length <= 7', '7 < Length <= 10', 'Length > 10'
	explode=(0.02, 0.02, 0.02, 0.02)
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'red']
	# Note this value is in percentage
	fracs = [le4, le7, le10, g10]
	fracs.sort()
	plt.pie(fracs, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, labeldistance=1.05)
	plt.title('Words ' + parameter.capitalize())
	plt.tight_layout()
	plt.axis('equal')
	plt.legend(labels, loc='best')
	plt.show()