# import nltk #people may not want to install this...?
# nltk.data.path.append('./nltk_data/') #this may need to change depending on when
# from nltk.corpus import stopwords

class SocialDataHelpers(object):
	
	def __init__(self):
		#as we add API calls classes and functions, we need to add them to this dictionary
		self.supportedGetTypes = {'search': self.search}

	def tweetEasy(self, getType, api_results):
		self.api_results = api_results
		self.getType = getType
		try:
			self.data = self.supportedGetTypes[getType]()
		except:
			print 'Not a supported GET request...yet'
		if len(self.api_results) < 1:
			print 'nothing in dataset'
			exit()
		return self.data
	
	def search(self):
		return Search(self.api_results)



class Search(object):

	def __init__(self, api_results):
		self.data = api_results

	def printResults(self):
		#maybe we can do a pretty print or DUMPS here
		print self.data

	def screenNames(self):
	 	return [s['user']['screen_name'] for s in self.data[self.data.index('statuses')]]

	def hashtags(self):
		hashtags_text = []
		for s in self.data[self.data.index('statuses')]:
			hashList = s['entities']['hashtags']
			if len(hashList)>1:
				tempList = list()
				for hashDict in hashList:
					tempList.append(hashDict['text'])
				hashtags_text.append(tempList)
		return hashtags_text



if __name__ == "__main__":
	sd = SocialDataHelpers()
	tw = sd.tweetEasy('search', [1,2,3])
	tw.printData()

	#this is what I'm aiming for with how to use this class
	# mydata.getDict('screenNames', 'hashtags_text')
	# mydata.getList('screenNames')

