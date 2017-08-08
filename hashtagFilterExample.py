'''A simple Python 3 filter for hashtags

original code (Python 2) from:
https://stackoverflow.com/questions/14156625/fetching-tweets-with-hashtag-from-twitter-using-python
'''
from twython import *

def auth():
	"""Return an authenticated twython object"""

	TWITTER_APP_KEY = '***' 
	TWITTER_APP_KEY_SECRET = '***' 
	TWITTER_ACCESS_TOKEN = '***'
	TWITTER_ACCESS_TOKEN_SECRET = '***'

	t = Twython(app_key=TWITTER_APP_KEY, 
		        app_secret=TWITTER_APP_KEY_SECRET, 
		        oauth_token=TWITTER_ACCESS_TOKEN, 
		        oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
	return t

def search(twyObj, query=None):
	#Search number limited to 450/quarter of hour
	stdquery=""
	if(query==None):
		query=stdquery
	search = twyObj.search(q=query,   
		              count=10)
	tweets = search['statuses']

	for tweet in tweets:
		print (tweet['id_str'], '\n', tweet['text'], '\n\n\n')
	return

def main():
	print("[+]hashtagFilterPy started")
	#Insert your query here
	customquery="#example"
	t=auth()
	search(t,query=customquery)
	return

if(__name__=='__main__'): 
	main()
	
