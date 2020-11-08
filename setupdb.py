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
	db.User.insert_many(user)

def populateGenre():
	db.Genre.insert_many(genre)



#User IDs start from 1000000
#Genre IDs start from 1000
#FactIDs start from 100000000