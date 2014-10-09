# import nltk 
# nltk.data.path.append('./tweetEasy/nltk_data/') #this may need to change depending on when
# from nltk.corpus import stopwords

import queryTwitter
import tweetEasy

q = 'common core'
c = 100
num_iterations = 5

commonCore = queryTwitter.SearchTwitter(q, c, num_iterations)
statuses = commonCore.runQuery()

search = tweetEasy.ParseSearch(statuses)
print search.getDict('hashtags', 'screen_name')





