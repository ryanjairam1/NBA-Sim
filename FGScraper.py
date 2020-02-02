import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scraper(y):
    #print(y)

    req = urllib.request.Request(
    y, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)



    client = urlopen(req)

    

    bbrHTML =client.read()
    client.close()
    bbrPageSoup=soup(bbrHTML, "lxml")
    #print("made it before bs")
    basketballRefLink = bbrPageSoup.find("div", {"class":"r"})

    for a in basketballRefLink.find_all('a', href=True):
        basketballRefLink = a['href']
        #print(a['href'])
        break

    #print(basketballRefLink)

    #opens connection, grabs page html
    
    client = urlopen(basketballRefLink)
    playerHTML =client.read()
    client.close()
    

    #does HTML parsing
    # print("fuck you andrew")
    playerPageSoup=soup(playerHTML, "lxml")

    playerFG = playerPageSoup.find(string = "FG%").find_next("p").find_next("p").get_text()

    return playerFG