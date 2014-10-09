<<<<<<< HEAD
class Search(object):

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
		self.dataTypes = {
			'tweetText': self.tweetText,
			'createdAt': self.createdAt,
			'hashtags': self.hashtags,
			'mentions': self.mentions,
			'users': self.userData
		}
		#important question is tying user data to status data points

	def getDict(self, key, value):
		d = dict()
		for s in self.data:
			#create a Search object for this one tweet
			s_search = Search(s)
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
			d[k].append(v)
		else:
			d[k] = list()
			d[k].append(v)
		return d
=======
# import nltk #people may not want to install this...?
# nltk.data.path.append('./nltk_data/') #this may need to change depending on when
# from nltk.corpus import stopwords

class SocialDataHelpers(object):
	
	#get the data and make sure its valid - this might be better as a parent that each one of the data parsing classes
	#could use, but then you have to remember all the data parsing classes names, etc.
	def __init__(self, getType, api_results):
		self.supportedGetTypes = {'search': self.search, 'followers/id': self.search}
		self.api_results = api_results
		self.helper = ''
		try:
			self.helper = self.supportedGetTypes[getType]()
		except:
			print getType,'Not a supported GET request...yet'
		if not self.api_results:
			print 'nothing in dataset'
			exit()

	#create and return the data parsing classes
	def search(self):
		return self

	def printData(self):
		#maybe we can do a pretty print or DUMPS here
		return self.data

	def getDict(self, key, value):
		#would like to return a dict of requested key and value pairs with this fucntion
		
		return key, value

class Search(SocialDataHelpers):

	def __init__(self, getType,api_results):
		SocialDataHelpers.__init__(self,getType,api_results)
		self.data = api_results
		#self.statuses = self.data['statuses'] #self.statuses is a list of dictionaries
		#self.users = [s['user'] for s in self.statuses] #self.users is a list of user dictionaries
		#important question is tying user data to status data points
>>>>>>> 3e242cfa6c713411c47affe8fb07b7ac2baeb91a

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
			return [h['text'] for h in self.entities['hashtags'] if h]

	def mentions(self):
		if type(self.entities) is list:
			return [m['screen_name'] for e in self.entities for m in e['user_mentions'] if m['screen_name']]
		else:
			return [m['screen_name'] for m in self.entities['user_mentions'] if m['screen_name']]

	#user level data points of interest, , feel free to add to these!
	def userData(self, dataType):
		if type(self.users) is list:
			return [s[dataType] for s in self.users if s[dataType]]
		else:
			if dataType in self.users.keys():
				return self.users[dataType]
			else:
				return ''

if __name__ == "__main__":
<<<<<<< HEAD
	import pickle
	testPickle = open('common core_1412823473.pk1', 'rb')
	data = pickle.load(testPickle)
	search = Search(data)
	# followers = SocialDataHelpers('twitter', 'followers/id', [4,5,6]).helper
	print search.getDict('hashtags', 'screen_name')
=======
	search = Search('search', [1,2,3])
	#followers = SocialDataHelpers('followers/id', [4,5,6]).helper
	print search.printData()
	#print followers.getDict('something', 'else')
>>>>>>> 3e242cfa6c713411c47affe8fb07b7ac2baeb91a

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

