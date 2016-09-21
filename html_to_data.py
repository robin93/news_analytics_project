import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "/home/robin/Desktop/hff_project/Data/Large Cap/ACC/ACC_1-31.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
mydivs = soup.findAll("div", { "class" : "article" })
# print len(mydivs)

meta_info_output_file = open('/home/robin/Desktop/hff_project/Data/Large Cap/ACC/ACC_meta.txt', 'w')
news_text_output_file = open('/home/robin/Desktop/hff_project/Data/Large Cap/ACC/ACC_news.txt','w')
news_heading_text_output_file = open('/home/robin/Desktop/hff_project/Data/Large Cap/ACC/ACC_news_headings.txt','w')


iteration = 0
for article in mydivs:
	iteration += 1
	# print "article number",iteration
	# print len(article)
	classes = article['class']
	if len(classes) == 2:
		print type(article)
		print len(article)
		# print article
		serial_div = 0
		serial_p = 0
		article_text = ""
		for tags in article:
			if tags.name in ['p','div']:
				if len(tags.attrs.keys()) > 0:
					if tags.attrs.keys()[0] == "id":
						heading = tags.text.strip()
			if tags.name == 'div':
				serial_div += 1
				# print serial_div,tags
				if serial_div == 2:
					length_of_article = tags.text
				if serial_div == 3:
					date = tags.text
				if serial_div == 4:
					time = tags.text
			if tags.name == 'p':
				serial_p += 1
				# print serial_p,tags
				# if serial_p == 3:
				# 	subheading = tags.text.strip()
				if serial_p > 2:
					article_text = article_text + " " + tags.text.strip()
		# print subheading
		print length_of_article
		print date
		print time
		print article_text
		article_text = article_text.replace('\n',' ')
		length_of_article = length_of_article.replace(' words','')
		number_of_words = len(article_text.split())
		# print article
		if number_of_words > int(length_of_article)*0.3:
			meta_info = length_of_article + "," + str(number_of_words) +","+ date + "," + time + "\n"
			news_text = article_text + "\n"
			heading_text = heading.replace('\n',' ') + "\n"
			meta_info_output_file.writelines(meta_info)
			news_text_output_file.writelines(news_text)
			news_heading_text_output_file.writelines(heading_text)
	print "\n\n\n"
	# if iteration > 5:
		# break



