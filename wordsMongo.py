from pymongo import MongoClient
client = MongoClient()

wordsDB = client['vocabulary-builder']

wordsCollection = wordsDB['words']

# Create collection if it does not exist
if wordsCollection.posts.count() != 4737:
	rawDB = open("Final Words DB", 'r')

	count = 1
	for line in rawDB:
		line = line.strip().split('\t')
		post = {"id" : count,
				"word" : str(line[0]),
				"defn" : str(line[1]),
				"use" : str(line[2]),
				"points" : int(line[3]),
				"diff" : int(line[4]),
				"origin" : str(line[5])
		}
		count += 1
		result = wordsCollection.posts.insert_one(post)
		
	rawDB.close()
	print "Words database created!"
else:
	print "Words database up-to-date"

print wordsCollection.posts.count()