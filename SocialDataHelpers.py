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

	#status data points of interest, feel free to add to these!
	def hashtags(self):
		return [hd['text'] for s in self.statuses for hd in s['entities']['hashtags']]

	def tweets(self):
		return [s['text'] for s in self.statuses]

	def createdAt(self):
		return [s['createdAt'] for s in self.statuses]

	#user level data points of interest, , feel free to add to these!
	def users(self):
		return [s['screen_name'] for s in self.users]

	def screenNames(self):
	 	return [s['screen_name'] for s in self.users]
	
	def descriptions(self):
		return [s['description'] for s in self.users]

	def profileImage(self):
		return [s['profile_image_url_https'] for s in self.users]

	def timeZone(self):
		return [s['time_zone'] for s in self.users]

	def followerCount(self):
		return [s['followers_count'] for s in self.users]

	def protected(self):
		return [s['protected'] for s in self.users]

	def geoEnabled(self):
		return [s['geo_enabled'] for s in self.users]

	def statusCount(self):
		return [s['stasuses_count'] for s in self.users]

	def friendsCounts(self):
		return [s['friends_count'] for s in self.users]

	def location(self):
		return [s['location'] for s in self.users]


if __name__ == "__main__":
	search = Search('search', [1,2,3])
	#followers = SocialDataHelpers('followers/id', [4,5,6]).helper
	print search.printData()
	#print followers.getDict('something', 'else')

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

