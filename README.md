Social Data Helpers
===================


sd = SocialData('API CALL TYPE', 'RESULTS OF CALL').helper

Get a list of all screennames for all statuses in search results like this:


screenNames = sd.screenNames()


Got rid fo the tweetEasy method since we are just using Twitter, I don't have an argument for service yet, but I imagine we can add one to handle Instagram.



