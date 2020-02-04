import random
#def offensivePossession(x,y,z,w):
  #  player = x
   # twoPTFG = y
    #threePTFG = z
    #typeOfShot = w
    #teamScore = 0
#
 #   twoPtRand = random.random()
 #   threePtRand = random.random()
 #   shotRand = random.random()
 #   
        #this is a 3 pt shot
   # if (shotRand <= typeOfShot):
     #   if(threePtRand <= threePTFG):
     #       teamScore = teamScore + 3

      #this is a 2 pt shot
    #else:
       # if(twoPtRand <= twoPTFG):
           # teamScore = teamScore + 2

    #return teamScore
    ##cale come to j beach


def game(l,m):
    fgList = l
    playerList = m

    player1Score = 0
    player2Score = 0
    targetscore = 15

    player1FG = float(fgList[0])/100
    player2FG = float(fgList[1])/100
    print(player1FG)
    print(player2FG)

    p1shotsMade = 0
    p1TotalShots = 0

    p2shotsMade = 0
    p2TotalShots = 0

    while player1Score or player2Score < targetscore:
    #player 1 shot attempt
        x = random.random()
        if (x < player1FG):
            #print("Player 1 made the shot!")
            player1Score = player1Score + 2
            p1shotsMade = p1shotsMade +1
            p1TotalShots = p1TotalShots +1
            #print("Player 1 score:", player1Score)
            if(player1Score >= targetscore):
                break
        else:
            #print("Player 1 missed the shot!")
            p1TotalShots = p1TotalShots +1
            #print("Player 1 score:", player1Score)
        y = random.random()
        if (y < player2FG):
            #print("Player 2 made the shot!")
            player2Score = player2Score + 2
            p2shotsMade = p2shotsMade +1
            p2TotalShots = p2TotalShots +1
            #print("Player 2 score:", player2Score)
            if(player2Score >= targetscore):
                break
        else:
            #print("Player 2 missed the shot!")
            p2TotalShots = p2TotalShots +1
        #  print("Player 2 score:", player2Score)
    print("final score: p1:", player1Score, "p2:", player2Score)
    
    if(player1Score>player2Score):
        print(playerList[0], " wins!")
    else:
        print(playerList[1], "  wins!")

    print(playerList[0], " FG% for the game:", round((p1shotsMade/p1TotalShots)*100,2), "%")
    print(playerList[1], " FG% for the game: ", round((p2shotsMade/p2TotalShots)*100,2), "%")

