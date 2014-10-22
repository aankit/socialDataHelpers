#!/usr/bin/env python
import sys, twitter, twitterKeys, pickle, time
	
class SearchTwitter(object):
	
	def __init__(self, q, c, num_iterations):
		#create twitter object, you should create your own twitterKeys.py file with your keys
		self.q = q
		self.c = c
		self.num_iterations = num_iterations
		auth = twitter.oauth.OAuth(twitterKeys.TOKEN, twitterKeys.TOKENSECRET, twitterKeys.KEY, twitterKeys.KEYSECRET) 
		self.tw_api = twitter.Twitter(auth=auth)

	# ---- Functions --------
	def get_rate_limit(self, t, call_type):
	    if call_type=='trends_place':
	        limit = t.application.rate_limit_status()
	        return limit['resources']['trends']['/trends/place']['remaining']
	    
	    elif call_type=='lists_memberships':
	        limit = t.application.rate_limit_status()
	        return limit['resources']['lists']['/lists/memberships']['remaining']

	def runQuery(self, save=False):
		search_results = self.tw_api.search.tweets(q=self.q, count=self.c)
		statuses = search_results['statuses']

		if self.num_iterations>1:
			for i in range(self.num_iterations):
				maxID = getMaxID(search_results)
				search_results = self.tw_api.search.tweets(q=self.q, count=self.c, max_id=maxID)
				statuses += search_results['statuses']

		current = time.time()
		if save:
			pickleName = '%s_%d.p' %(self.q, current)
			output = open(pickleName, 'wb')
			pickle.dump(statuses, output)
		else:
			return statuses

	def getMaxID(self, search_results):
		params = {a:b for a,b in [x.split('=') for x in search_results['search_metadata']['next_results'][1:].split('&')]}
   		return int(params['max_id'])

if __name__ == '__main__':
	try:
		q = sys.argv[1]
		c = sys.argv[2]
		num_iterations = int(sys.argv[3])
	except:
		print "please enter a search string, number of statuses up to 100, and number of requests, up to 180(?)"

	search = SearchTwitter(q, c, num_iterations)
	print search.runQuery()