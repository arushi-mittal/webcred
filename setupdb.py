from pymongo import MongoClient
import random
import datetime

client = MongoClient('localhost', 27017)

db = client.webcred

def populateFact ():
	fact = []
	sites = ["randomlists.com/websites", "surveymonkey.com", "jalbum.net", "npr.org", "last.fm"]
	for i in range(5):
		fact[i] = {"FactID": 100000000 + i,
					"URL": sites[i],
					"GenreID": random.randint(1000, 1010),
					"S_Score": random.randint(0, 10),
					"C_Score": random.randint(0, 10),
					"O_Score": random.randint(0, 10),
					"A_Score": random.randint(0, 10),
					"Time": datetime.now()
				  }
	db.Fact.insert_many(fact)


def populateUser ():
	user = []
	for i in range(5):
		user[i] = {"UserID": 1000000 + i,
				   "Email": str(i) + "@example.com",
				   "GenreID": random.randint(1000, 1010),
		"tld": random.randint(0, 100),
		"brokenlinks": random.randint(0, 100),
		"internallinks": random.randint(0, 100),
		"externallinks": random.randint(0, 100),
		"advertisements": random.randint(0, 100),
		"pageloadtime": random.randint(0, 100),
		"responsiveness": random.randint(0, 100),
		"lastmodified": random.randint(0, 100),
		"internationalized": random.randint(0, 100),
		"email": random.randint(0, 100),
		"socialmedia": random.randint(0, 100),
		"textimageratio": random.randint(0, 100),
		"subjectivity": random.randint(0, 100),
		"polarity": random.randint(0, 100),
		"internationalized": random.randint(0, 100),
		"grammarerrors": random.randint(0, 100),
		"spellingerrors": random.randint(0, 100),
		"nouns": random.randint(0, 100),
		"verbs": random.randint(0, 100),
		"adjectives": random.randint(0, 100),
		"adverbs": random.randint(0, 100),
		"pronouns": random.randint(0, 100),
		"backlinks":random.randint(0, 100),
					"Time": datetime.now()

				  }

	db.User.insert_many(user)

def populateGenre():
	genre = []
	names = ["Educational", "Shopping", "Social Media", "Research", "Other"]
	for i in range(5):
		genre[i] = {"GenreID": random.randint(1000, 1010),
					"GenreName":names[i],
					"Time": datetime.now()
				   }
	db.Genre.insert_many(genre)



#User IDs start from 1000000
#Genre IDs start from 1000
#FactIDs start from 100000000