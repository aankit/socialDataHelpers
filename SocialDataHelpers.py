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
			print 'Not a supported GET request...yet'
		if len(self.api_results) < 1:
			print 'nothing in dataset'
			exit()

	#create and return the data parsing classes
	def search(self):
		return Search(self.api_results)

	def printData(self):
		#maybe we can do a pretty print or DUMPS here
		return self.data

	def getDict(self, key, value):
		#would like to return a dict of requested key and value pairs with this fucntion
		return key, value

class Search(SocialDataHelpers):

	def __init__(self, api_results):
		self.data = api_results
		#self.statuses = self.data['statuses']

	def screenNames(self):
	 	print 'asshole'
	 	# return [s['user']['screen_name'] for s in self.statuses]

	def hashtags(self):
		return [hd['text'] for s in self.statuses for hd in s['entities']['hashtags']]

	def tweets(self):
		return [s['text'] for s in self.statuses]

	def users(self):
		return [s['user']['screen_name'] for s in self.statuses]

	def descriptions(self):
		return [s['user']['description'] for s in self.statuses]


if __name__ == "__main__":
	search = SocialDataHelpers('search', [1,2,3]).helper
	followers = SocialDataHelpers('followers/id', [4,5,6]).helper
	print search.printData()
	print followers.getDict('something', 'else')

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

