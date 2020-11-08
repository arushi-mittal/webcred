import requests
from bs4 import BeautifulSoup
import urllib.request
import tldextract
from adblockparser import AdblockRules
from time import time
from htmldate import find_date
import subprocess
import json
from textblob import TextBlob, Word
from grammarbot import GrammarBotClient
import spacy
from pymongo import MongoClient
import datetime
from selenium import webdriver
import re
from sys import getsizeof
print('Enter URL')
url = input()
def getdomain (url, tld):
	return tldextract.extract(url).domain + tld
def getpagedata (url):
	response = requests.get(url)
	headers = response.headers
	soup = BeautifulSoup(response.text, 'html.parser')
	return (headers, soup)
def getlinks (pagedata):
	anchors = pagedata.find_all('a')
	links = []
	for anchor in anchors:
		if anchor.get('href'):
			links.append(anchor.get('href'))
	return links
def getplaintext(pagedata):
	for script in pagedata(['script', 'style']):
		script.extract()
	return pagedata.get_text()
def gettld (url):
	return '.' + tldextract.extract(url).suffix
def countlinks (links, domain, rules):	
	broken = 0
	internal = 0
	external = 0
	ads = 0
	socialmedia = ['instagram', 'twitter', 'facebook', 'github', 'gitlab', 'glassdoor']
	contact = []
	for link in links:	
		try:
			req = urllib.request.Request(url=link)
			resp = urllib.request.urlopen(req)
			if resp.status in [400,404,403,408,409,501,502,503]:
				broken = broken + 1
			else:
				if link.startswith('#'):
					continue
				elif link.startswith('/'):
					internal = internal + 1
				elif domain in link:
					internal = internal + 1
				else:
					external = external + 1
					for social in socialmedia:
						if social in link:
							contact.append(link)

				if rules.should_block(link):
					ads = ads + 1
		except:
			broken = broken + 1
			pass
		return (broken, internal, external, ads, contact)
def getadsrules ():
	response = requests.get('https://easylist.to/easylist/easylist.txt')
	raw_rules = response.text.split('\n')
	rules = AdblockRules(raw_rules)
	return rules
def pageloadtime (url):	
	stream = urllib.request.urlopen(url)
	start = time()
	stream.read()
	end = time() - start
	return end
def internationalization (pagedata, headerdata):
	html = pagedata.find('html')
	if html.has_attr('lang'):
		if html['lang'] != None:
			internationalized = True
	if internationalized == False:
		links = pagedata.find_all('link')
		for link in links:
			if link.has_attr('hreflang'):
				if link['hreflang'] != None:
					internationalized = True
	if internationalized == False:
		if 'Content-Language' in headerdata:
			if headerdata['Content-Language'] != None:
				internationalized = True
	return internationalized
def getresponsiveness(url):
    api_url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run'
    response = requests.post(api_url, json = {'url': url, 'requestScreenshot' : False}, params={'fields': 'mobileFriendliness', 'key': 'AIzaSyD5cxljYx_MGZER7qkiNFMMTLkAGW2VS1Q'})
    response = response.json()
    state = 0
    try:
	    if response["mobileFriendliness"] == 'MOBILE_FRIENDLY':
	        state = 1
	    else:
	    	state = 0
    except KeyError:
        print(logger.warning(response['error']['message']))
        state = 0
    return state
def getdatetime (pagedata, headerdata):
	d = ['Date', 'date']
	lm = ['last-modified', 'last-Modified', 'Last-Modified', 'Last-modified']
	for k in headerdata:
		for l in lm:
			if l in k:
				return headerdata[k]
	out = subprocess.Popen(['https', '-h', url], stdout = subprocess.PIPE)
	out = out.stdout.readlines()
	for line in out:
		for l  in lm:
			if l in str(line):
				return line.decode("utf-8")[20::]
	if find_date(url):
		return find_date(url)
	for line in out:
		for date in d:
			if date in str(line):
				return line.decode("utf-8")[11::]
def getemail (plaintext):
	regexemail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	lines = plaintext.split('\n')
	emails = []
	for line in lines:
		words = line.split(' ')
		for word in words:
			if re.search(regexemail, word):
				emails.append(word)
	if emails == None:
		return "Not Available"
	return emails
def getimagetextratio (pagedata, domain, plaintext, tld):	
	img_tags = pagedata.find_all('img')
	imglinks = [img['src'] for img in img_tags]
	imgsize = 0
	for img in imglinks:
		if img.startswith('/'):
			if tldextract.extract(img).suffix != tld:
				img = 'https://' + domain + img
			else:
				img = 'https:' + img
		try:
			imgsize = imgsize + len(urllib.request.urlopen(img).read())
		except:
			continue
	plaintextsize = getsizeof(plaintext)
	if plaintextsize == 0:
		return 100
	else:
		return imgsize/plaintextsize
def getspellingerrors (plaintext):
	plaintext = plaintext.split(' ')
	misspelled = 0
	for word in plaintext:
		s = ""
		for letter in word:
			if letter.isalpha():
				s = s + letter
		if Word(s).correct() != s:
			misspelled = misspelled + 1
	return misspelled
def getsentiment (plaintext):
	text = TextBlob(plaintext)
	polarity = text.sentiment.polarity
	subjectivity = text.sentiment.subjectivity
	return (polarity, subjectivity)
def getgrammarerrors (plaintext):
	client = GrammarBotClient()
	res = client.check(plaintext)
	return(len(res.matches))
def getpos (plaintext):
	poss = ['NOUN', 'VERB', 'ADJ', 'ADV', 'ADP', 'PRON']
	count = {'NOUN': 0, 'VERB' : 0, 'ADJ' : 0, 'ADV' : 0, 'ADP' : 0, 'PRON' : 0}
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(plaintext)
	for token in doc:
		if token.pos_ in poss:
			count[token.pos_] = count[token.pos_] + 1
	return count
def getbacklinks (url):
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--incognito')
	options.add_argument('--headless')
	driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
	driver.get("http://www.google.com/search?q=link:" + url)
	results = driver.find_element_by_id('result-stats')
	soup = BeautifulSoup(results.text, features = "lxml")
	li = soup.find('p').get_text()
	return li.split(' ')[1]
pagedata = getpagedata(url)
headers = pagedata[0]
pagedata = pagedata[1]
plaintext = getplaintext(pagedata)
links = getlinks(pagedata)
tld = gettld(url)
domain = getdomain(url, tld)
def writetodatabse ():
	global url, pagedata, headers, plaintext, links, tld, domain, rules
	rules = getadsrules()
	client = MongoClient('localhost', 27017)
	db = client.webcred
	linklist = countlinks(links,domain, rules)
	sentiment = getsentiment(plaintext)
	pos = getpos(plaintext)
	postfact = {
		"tld": tld,
		"brokenlinks": linklist[0],
		"internallinks": linklist[1],
		"externallinks": linklist[2],
		"advertisements": linklist[3],
		"pageloadtime": pageloadtime(url),
		"responsiveness": getresponsiveness(url),
		"lastmodified": getdatetime(pagedata, headers),
		"internationalized": internationalization(pagedata, headers),
		"email": getemail(plaintext),
		"socialmedia": linklist[4],
		"textimageratio": getimagetextratio(pagedata, domain, plaintext, tld),
		"subjectivity": sentiment[1],
		"polarity": sentiment[0],
		"internationalized": internationalization(pagedata, headers),
		"grammarerrors": getgrammarerrors(plaintext),
		"spellingerrors": getspellingerrors(plaintext),
		"nouns": pos['NOUN'],
		"verbs": pos['VERB'],
		"adjectives": pos['ADJ'],
		"adverbs": pos['ADV'],
		"pronouns": pos['PRON'],
		"backlinks": getbacklinks(url)
	}
	db.Feature.insert_one(postfact)
writetodatabse()