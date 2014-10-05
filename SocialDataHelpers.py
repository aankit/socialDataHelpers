# import nltk #people may not want to install this...?
# nltk.data.path.append('./nltk_data/') #this may need to change depending on when
# from nltk.corpus import stopwords

class SocialDataHelpers(object):
	
	#get the data and make sure its valid - this might be better as a parent that each one of the data parsing classes
	#could use, but then you have to remember all the data parsing classes names, etc.
	def __init__(self, getType, api_results):
		self.supportedGetTypes = {'search': self.search, 'followers/id': self.search}
		self.api_results = api_results
		self.data = 0
		try:
			self.data = self.supportedGetTypes[getType]()
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

class Search(SocialDataHelpers):

	def __init__(self, api_results):
		self.data = api_results
		#self.statuses = self.data['statuses']

	def screenNames(self):
	 	return [s['user']['screen_name'] for s in self.statuses]

	def hashtags(self):
		hashtags_text = []
		for s in self.statuses:
			hashList = s['entities']['hashtags']
			if len(hashList)>1:
				tempList = list()
				for hashDict in hashList:
					tempList.append(hashDict['text'])
				hashtags_text.append(tempList)
		return hashtags_text

	def tweets(self):
		return [s['text'] for s in self.statuses]

	def users(self):
		return [s['user']['screen_name'] for s in self.statuses]

	def descriptions(self):
		return [s['user']['description'] for s in self.statuses]


if __name__ == "__main__":
	search = SocialDataHelpers('search', [1,2,3]).data
	followers = SocialDataHelpers('followers/id', [4,5,6]).data
	# tw = sd.tweetEasy('search', [1,2,3])
	print search.printData()
	print followers.printData()

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

