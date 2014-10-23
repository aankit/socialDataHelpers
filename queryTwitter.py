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

	def get_country_woeid_dict(self,woeid_list):

		 new_country_dict = {}

		 if not woeid_list:
		 	raise Exception("Country list empty")

		 for w_id in woeid_list:
		 	new_country_dict[w_id['name']] = w_id['woeid']

		 return new_country_dict

	def trends(self,country_dict=None,country_or_place_id=None):
		if country_or_place_id:
			if isinstance(country_or_place_id,int):
				return self.tw_api.trends.place(_id=country_or_place_id)
			
			elif isinstance(country_or_place_id,(str,unicode)):
				if not country_dict:
					raise Exception("Places dictionary empty")
				woeid = country_dict[country_or_place_id]
				if not woeid:
					raise Exception("Place not in dictionary")
				return self.tw_api.trends.place(_id=woeid)

			else: raise Exception("Cannot recognize - ",country_or_place_id)
			
		return self.tw_api.trends.place(_id=1)


	""" Returns countries woeid list from twitter.
		This can be used instead of loading countries data from file"""
	def get_countries_woeid_list_from_twitter(self):
		return self.twitter_api.trends.available()

if __name__ == '__main__':
	try:
		q = sys.argv[1]
		c = sys.argv[2]
		num_iterations = int(sys.argv[3])
	except:
		print "please enter a search string, number of statuses up to 100, and number of requests, up to 180(?)"

	search = SearchTwitter(q, c, num_iterations)
	print search.runQuery()