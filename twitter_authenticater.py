import twitter




OAUTH_TOKEN='Your OAUTH_TOKEN'
OAUTH_TOKEN_SECRET='Your OAUTH_TOKEN_SECRE'
CONSUMER_SECRET='Your CONSUMER_SECRET'
CONSUMER_KEY='Your CONSUMER_KEY'


class TwitterAuthinticater:
	"""docstring for ClassName"""

	def __init__(self):
		pass

	def authnticate(self):

		auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

		twitter_api=twitter.Twitter(auth=auth)

		return twitter_api



if __name__ == "__main__":

	twitter_auth=TwitterAuthinticater()
	twitter_api=twitter_auth.authnticate()
	print(twitter_api)
		
		