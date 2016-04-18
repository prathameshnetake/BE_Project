import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import statistics as stat
from wordcloud import WordCloud
from pymongo import MongoClient
client = MongoClient()

usersDB = client['vocabulary-builder']
users = usersDB['users']
result = usersDB['train-result']
words = usersDB['words']

def fancyStats():
	"""
	Base function for statistics about the words database
	"""
	origin = []
	usage = []
	points = []
	diff = []
	allWords = words.posts.find({}, {'origin':1, 'use':1, 'points':1, 'diff':1})
	for word in allWords:
		origin.append(word['origin'])
		usage.append(word['use'])
		points.append(word['points'])
		diff.append(word['diff'])
	d = {'origin' : origin, 'use' : usage, 'points' : points, 'diff' : diff}
	return d

def pointsHist(points):
	# Generates histogram for points
	mean = round(stat.mean(points), 2)
	median = round(stat.median(points), 2)
	mode = round(stat.mode(points), 2)
	var = round(stat.variance(points), 2)
	stdDev = round(stat.stdev(points), 2)
	
	num_bins = 12
	plt.hist(points, num_bins, alpha=0.5)
	plt.axvline(mean, color='r', linestyle='solid', linewidth=2, label='Mean')
	plt.axvline(median, color='g', linestyle='--', linewidth=2, label='Median')
	plt.axvline(mode, color='c', linestyle='-.', linewidth=2, label='Mode')
	plt.xlabel('Points')
	plt.ylabel('# words')
	plt.title('Histogram of points')
	plt.text(35, 1050,'Variance = ' + str(var), ha='center', va='center')
	plt.text(35, 1000,'Std Dev = ' + str(stdDev), ha='center', va='center')
	plt.legend()
	plt.show()

# d = fancyStats()
# pointsHist(d['points'])

def counterStat(parameter):
	"""
	Generates statistics for parameter
	parameter: origin or use
	"""
	count = dict(Counter(parameter)).items()
	count.sort(key=lambda (k, v) : (-v))
	for k, v in count:
		print '%s : %d' % (str(k), v)

# d = fancyStats()
# counterStat(d['use'])
# counterStat(d['origin'])

def wordCloud(username, parameter):
	"""
	Generates a word cloud based on the parameter for specified username
	parameter : total, correct, wrong
	"""
	userWord = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
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
	userWord = users.posts.find_one({'username' : username}, {'username' : 0,
															'name' : 0,
															'userType' : 0,
															'secret' : 0,
															'_id' : 0})
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