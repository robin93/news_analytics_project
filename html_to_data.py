import urllib
from bs4 import BeautifulSoup

# input_text = open('Factiva_wipro.html','r+')



# print input_text


url = "Factiva_wipro.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"lxml")

# print type(soup)

# print soup.get_text()

# print soup.prettify()

# row =  soup.find_all('span', string='')

# loop = 0
# for r in row:
# 	loop += 1
# 	# print loop
# 	# print r

# pages = soup.find_all('p', string='')

# loop2 = 0
# for page in pages:
# 	# print pages
# 	loop2 += 1
# 	# print loop2


mydivs = soup.findAll("div", { "class" : "article" })

# print len(mydivs)



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
						print tags.text.strip()
			if tags.name == 'div':
				serial_div += 1
				if serial_div == 4:
					length_of_article = tags.text
				if serial_div == 5:
					date = tags.text
				# if len(tags.attrs.keys()) > 0:
				# 	print tags.attrs
				# 	print "\n"
				# print tags
			if tags.name == 'p':
				serial_p += 1
				if serial_p == 3:
					subheading = tags.text.strip()
				if serial_p > 3:
					article_text = article_text + " " + tags.text.strip()
		print subheading
		print length_of_article
		print date
		print article_text
	# print article['class']
	# for lines in article:
	# 	print lines
	# 	if lines.name in ["p","div"]:
	#  		print type(lines)
	#  		print lines.name
	#  		print lines.id
	#  	# print lines["class"]
	# # div_tags = article.findAll("div")
	# # print "number of div_tags",len(div_tags)
	# # p_tags = article.findAll("p")
	# # print "number of p tags",len(p_tags)
	print "\n\n\n"
	if iteration > 1:
		break



