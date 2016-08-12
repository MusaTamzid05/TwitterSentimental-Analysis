from tweets import Tweets
from file_io import File_IO


'''

Use this class to create postive and negative tweets for a given movie
and write it in a text file.
'''


class TweetLabeler:

	def __init__(self,tweets):
		

		self.tweets=tweets
		# need to improve this words
		self.positive_words=['good','great','awesome','Fantastic','10/10','rock','rocks','happy','amazing','love','watching','more','interesting','nice',
		                    'times','adorable','cute','hit','cool','king']


	def get_label_tweets(self):

		label_tweets=[]

		


		for tweet in self.tweets:
			
			for word in self.positive_words:

				



				if word.lower() in tweet.lower():
					label_tweets.append((tweet,"pos"))
					break


			else:
				label_tweets.append((tweet,"neg"))

		return label_tweets

	def get_positive_negativate_tweets(self):

		label_tweets=self.get_label_tweets()

		pos_tweets,neg_tweets=[],[]

		for tweet in label_tweets:

			if tweet[1] == 'pos':
				pos_tweets.append(tweet[0])

			else:
				neg_tweets.append(tweet[0])


		return pos_tweets,neg_tweets



def main():


	tweets=Tweets()
	tweets=tweets.search_tweets('#AngryBirdsMovie')

	if tweets  == None:
		print("No tweets")
		exit(1)


	tweetLabeler=TweetLabeler(tweets)

	pos_tweets,neg_tweets=tweetLabeler.get_positive_negativate_tweets()

	print("Total postive tweets:{}".format(len(pos_tweets)))
	print("Total negatibe tweets:{}".format(len(neg_tweets)))


	

	

	f_io=File_IO()

	f_io.write_file('pos.txt',pos_tweets)
	f_io.write_file("neg.txt",neg_tweets)
	f_io.readLines('pos.txt')
	f_io.readLines("neg.txt")

	




if __name__ == "__main__":

	main()


		