class ParseSearch(object):

	def __init__(self, statuses):
		self.data = statuses #self.statuses is a list of dictionaries
		if type(self.data) is dict:
			self.users = self.data['user']
			self.entities = self.data['entities']
		else:
			self.users = [s['user'] for s in self.data] #self.users is a list of user dictionaries
			self.entities = [s['entities'] for s in self.data]
			self.retweets = [s['retweeted_status'] for s in self.data if 'retweeted_status' in s.keys()]
			# print self.retweets
		# self.Retweets = Search(self.retweets)
		# I can structure by status, entity, and user
		self.dataTypes = {
			'tweetText': self.tweetText,
			'createdAt': self.createdAt,
			'hashtags': self.hashtags,
			'user_mentions': self.user_mentions,
			'users': self.userData
		}

	def getDict(self, key, value):
		d = dict()
		for s in self.data:
			#create a Search object for this one tweet
			s_search = ParseSearch(s)
			#use the dataTypes dict to get the key and value for this one tweet
			if key in s_search.dataTypes.keys():
				k = s_search.dataTypes[key]()
			else:
				k = s_search.dataTypes['users'](key)
			if value in s_search.dataTypes.keys():
				v = s_search.dataTypes[value]()
			else:
				v = s_search.dataTypes['users'](value)
			#if the key is a list - i.e hastags, mentions, maybe more stuff
			if type(k) is list:
				for i in k:
					d = self.makeDict(d, i, v)
			else:
				d = self.makeDict(d, k, v)
		return d

	def makeDict(self, d, k, v):
		if k in d.keys():
			if type(v) is list and len(v)>0:
				for i in v:
					d[k].append(v)
			elif v!=None:	
				d[k].append(v)
		else:
			if type(v) is list and len(v)>0:
				d[k] = v
			elif v!=None:
				d[k] = [v]
		return d

	#status data points of interest, feel free to add to these!
	def tweetText(self):
		if type(self.data) is list:
			return [s['text'] for s in self.data]
		else:
			return self.data['text']

	def createdAt(self):
		if type(self.data) is list:
			return [s['created_at'] for s in self.data]
		else:
			return self.data['created_at']

	#entities data points of interest
	def hashtags(self):
		if type(self.entities) is list:
			return [h['text'] for e in self.entities for h in e['hashtags'] if h]
		else:
			for h in self.entities['hashtags']:
				if h['text'] != None:
					return h['text']
				else:
					pass

	def user_mentions(self):
		if type(self.entities) is list:
			return [m['screen_name'] for e in self.entities for m in e['user_mentions'] if m['screen_name']]
		else:
			return [m['screen_name'] for m in self.entities['user_mentions'] if m['screen_name']]

	#user level data points of interest, includes all
	#
	def userData(self, dataType):
		if type(self.users) is list:
			return [s[dataType] for s in self.users if s[dataType]]
		else:
			if dataType in self.users.keys():
				return self.users[dataType]
			else:
				return ''

if __name__ == "__main__":
	import pickle
	testPickle = open('common core_1412823473.pk1', 'rb')
	data = pickle.load(testPickle)
	search = ParseSearch(data)
	# followers = SocialDataHelpers('twitter', 'followers/id', [4,5,6]).helper
	print search.getDict('hashtags', 'screen_name')

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

