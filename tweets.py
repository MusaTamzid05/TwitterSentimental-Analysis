from twitter_authenticater import TwitterAuthinticater
import json


class Tweets:

	def __init__(self):
		
		auth=TwitterAuthinticater()
		self.twitter_api=auth.authnticate()


	def search_tweets(self,quary_name,total_tweet_count=100):

		


		

		if quary_name.startswith('#') ==False:
			quary_name='#' +quary_name

		search_results=self.twitter_api.search.tweets(q=quary_name,count=total_tweet_count)


		if len(search_results) == 0:
			print("No tweets found")
			return None

		statuses=search_results['statuses']


		'''

		This code here goes through 5 more branches of the results
		so that we can get more tweets.

		'''


		for _ in range(5):

			

			try:
				
				next_results=search_results['search_metadata']['next_results']
			

			except KeyError:
				break


			# creating a dictionary from the next results which has the following form
			# ?max_id=313519052523986943&q=NCAA&include_entities=1

			kwargs=dict([kv.split('=') for kv in next_results[1:].split('&')])
			#print(next_results)
			
			#print("......")


			search_results=self.twitter_api.search.tweets(**kwargs)
			statuses += search_results['statuses']

			'''
			The whole loop code  above is from the book  "Mining the Social Web 2nd ed"
			Amaing book!!!Best API book ever!!

			'''

			text=self._get_text(statuses)


			return text







			#print("Save statuses")


	def _get_text(self,statuses):
		

		return set(status['text'] for status in statuses)
	


		

		
		

		



if __name__ == "__main__":


	tweets=Tweets()
	tweets=tweets.search_tweets('#Suicide Squad')

	for tweet in tweets:
		print(tweet)


