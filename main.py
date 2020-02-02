#ask user for the name of the player they want
#send a request to https://www.google.com/search?q= followed by the "Basketball Reference" followed by first name and then last name
#then get the first google link
#then use your FGScraper to get their FG%

from gamePlayed import game
from FGScraper import scraper

playerList=[]
fgList=[]
player1 = input("Enter the name of player 1:")
playerList.append(player1.replace(" ", ""))
player2 = input("Enter the name of player 2:")
playerList.append(player2.replace(" ", ""))

for x in playerList:
    link2Scrape = "https://www.google.com/search?q=basketballreference"+ x
    fgList.append(scraper(link2Scrape))

game(fgList, playerList)


