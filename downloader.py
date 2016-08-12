from  urllib.request import urlopen
import re





class Downloader:

	def __init__(self):

		pass


	

	def download(self,url):

		html=None


		try:

			html=urlopen(url).read().decode()

		except Exception as e:

			print(e)


		return html


	def imdb_review_download(self,url):

		html=None

		pattern='^http:\/\/www\.imdb\.com\/title\/[a-z0-9].+\/reviews\?ref_=.+'

		if re.match(pattern,url) == False:

			print("The url is not of a imdb review page")
			return None

		else:

			html=self.download(url)

		return html









if __name__ == "__main__":

	

	downloader=Downloader()

	


	html=downloader.imdb_review_download('http://www.imdb.com/title/tt0021749/?ref_=adv_li_tt')

	if html!= None:
		print(html)