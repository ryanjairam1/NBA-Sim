from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup
URL = "https://www.basketball-reference.com/players/j/jamesle01.html"
#opens connection, grabs page html
client = urlReq(URL)
lebronHTML =client.read()
client.close()
#does HTML parsing
lebronPageSoup=soup(lebronHTML, "lxml")
print(lebronPageSoup.h4)
#lebronFG=lebronPageSoup.find(string = "Field Goal Percentage").find_next("p").get_text()
#print(lebronFG)

lebronFG = lebronPageSoup.find(string = "FG%").find_next("p").find_next("p").get_text()
print(lebronFG)