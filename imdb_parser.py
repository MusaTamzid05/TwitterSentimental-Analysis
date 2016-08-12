from bs4 import BeautifulSoup
from downloader import Downloader


'''
Give a html of a imdb movie review page and this will get all the reviews of that 
movie from that page.

Warrning:The way it gets the review is hard coded,at the time i wrote the code it was working 
find but it will  fail in the future.


'''

class IMDB_Parser:


	def __init__(self,html):

		try:


			self.bsObj=BeautifulSoup(html,"html.parser")
			print("Parsing complete")
			print(self.bsObj.title)

		except Exception as e:
			print(e)


	def get_movie_reviews(self):

		try:


			movie_reviews=None

			body=self.bsObj.find("body")
			main_div=body.find("div")
			root_div=main_div.find("div")
			root_layer=main_div.find("layer")
			page_content=root_layer.find("div",{"id":"pagecontent"})
			reviews_div=page_content.find("div",{"class":"reviews"})
			contents=reviews_div.find("div",{"id":"tn15content"})
			reviews=contents.find_all("p")

			movie_reviews=[]

			for review in reviews:
				movie_reviews.append(review.get_text())


			
		except Exception  as e: # use a better exception!!

			print(e)

		return movie_reviews







if __name__ == "__main__":

	downloader=Downloader()
	html=downloader.download("http://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv")

	if html == None:
		exit(2)


	parser=IMDB_Parser(html)

	movie_reviews=parser.get_movie_reviews()

	if movie_reviews:

		for review in movie_reviews:
			print(review)


	
