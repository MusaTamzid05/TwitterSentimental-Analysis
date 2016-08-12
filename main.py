from data_preaparer import Data_Preparer

import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier





if __name__ == "__main__":


	'''
	Use  tweetLabeler to create your own pos.txt and neg.txt.

	'''

	data_parser=Data_Preparer()
	pos_train,pos_test=data_parser.create_train_test_data('pos.txt','pos')
	neg_train,neg_test=data_parser.create_train_test_data('neg.txt','neg')

	print("pos train:{}".format(len(pos_train)))
	print("pos test:{}".format(len(pos_test)))

	print("neg train:{}".format(len(neg_train)))
	print("neg test:{}".format(len(neg_test)))

	


	

	
	


	

	tweets=data_parser.get_prepare_tweets(pos_train,neg_train)


	word_features=data_parser.get_word_features(data_parser.get_words_in_tweets(tweets))


	tranining_set=nltk.classify.util.apply_features(data_parser.extract_features,tweets)

	classifier=NaiveBayesClassifier.train(tranining_set)

	test_tweets=pos_test+neg_test

	total_tweets=len(test_tweets)




	accurate=0

	

	for tweet in test_tweets:

		if classifier.classify(data_parser.extract_features(nltk.word_tokenize(tweet[0])))==tweet[1]:
			accurate+=1


	print("Accuracy:{}/{}".format(accurate,total_tweets))





