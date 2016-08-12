from file_io import File_IO

import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier




'''
The original code that l  learn the segmantation from..
https://github.com/victorneo/Twitter-Sentimental-Analysis/blob/master/classification.py
Please see that code inorder to understand how it works.I have used  functions
get_word_features,extract_fatures,get_words_from_tweets from there.
That code example is really good !! 
'''


words_features=None

class Data_Preparer:

	def __init__(self):

		self.words_features=None

	def  create_train_test_data(self,file_name,label_name):
		

		file_io=File_IO()

		lines=file_io.getLines(file_name)


		if len(lines) == 0:
			print("There is no line in the file.")
			return

		train,test=self._test_train_spliter(lines,label_name)

		return train,test



	def _test_train_spliter(self,data,label):


		'''
		70 % of the data will be train data and 30% of the data will be test data.

		'''

		total_data=len(data)

	
		divide_index=int((70/100)*total_data)

		train_data,test_data=[],[]

		
		for index,line in enumerate(data):

			if index <= divide_index-1:
				train_data.append((line,label))

			else:
				test_data.append((line,label))


		return train_data,test_data


	def get_word_features(self,wordlist):

		wordlist=nltk.FreqDist(wordlist)

		word_features=wordlist.keys()

		return word_features


	def extract_features(self,document):

		document_words=set(document)
		features={}

		

		for word in self.word_features:

			features["contains {}".format(word)]=(word in document_words)

		return features

	def get_words_in_tweets(self,tweets):


		all_words=[]

		for (words,segment) in tweets:
			all_words.extend(words)

		return all_words





	def get_prepare_tweets(self,pos_tweets,neg_tweets):

		tweets=[]

		for (words,segment) in pos_tweets+neg_tweets:

			'''
			Any words that has length better than 3 are taken

			'''

			word_filter=[e.lower() for e in words.split() if len(e) >= 3]
			tweets.append((word_filter,segment))

		self.word_features=self.get_word_features(self.get_words_in_tweets(tweets))

		
		


		return tweets


		








if __name__ == "__main__":

	data_parser=Data_Preparer()
	pos_train,pos_test=data_parser.create_train_test_data('pos.txt','pos')
	neg_train,neg_test=data_parser.create_train_test_data('neg.txt','neg')

	print("pos train:{}".format(len(pos_train)))
	print("pos test:{}".format(len(pos_test)))

	print("neg train:{}".format(len(neg_train)))
	print("neg test:{}".format(len(neg_test)))

	


	

	
	


	

	tweets=data_parser.get_prepare_tweets(pos_train,neg_train)
	


	tranining_set=nltk.classify.util.apply_features(data_parser.extract_features,tweets)

	classifier=NaiveBayesClassifier.train(tranining_set)

	test_tweets=pos_test+neg_test

	total_tweets=len(test_tweets)




	accurate=0

	

	for tweet in test_tweets:

		if classifier.classify(data_parser.extract_features(nltk.word_tokenize(tweet[0])))==tweet[1]:
			accurate+=1


	print("Accuracy:{}/{}".format(accurate,total_tweets))





