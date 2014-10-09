import sys, twitter, twitterKeys, pickle, time
	
class Search(object):
	
	def __init__(self, q, c, num_iterations):
		#create twitter object
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

	def runQuery(self):
		search_results = self.tw_api.search.tweets(q=q, count=c)
		statuses = search_results['statuses']

		if num_iterations>1:
			for i in range(num_iterations):
				maxID = search_results['search_metadata']['max_id']-1
				search_results = self.tw_api.search.tweets(q=q, count=c, max_id=maxID)
				statuses += search_results['statuses']

		current = time.time()

		pickleName = '%s_%d.pk1' %(q, current)

		output = open(pickleName, 'wb')
		pickle.dump(statuses, output)

if __name__ == '__main__':
	try:
		q = sys.argv[1]
		c = sys.argv[2]
		num_iterations = int(sys.argv[3])
	except:
		print "please enter a search string, number of statuses up to 100, and number of requests, up to 180(?)"

	search = Search(q, c, num_iterations)
	search.runQuery()