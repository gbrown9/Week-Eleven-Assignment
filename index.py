# Gabe Brown
# Collaberated with Dr. Nuemann and Devin Simoneaux and Tyler Brown
# IWU - CIS - 125
# Week 11 Assignment



from BowlingGame import Game
# Call and read scores
file = open("testscores.txt", "r")


for line in file:
    
    line = line.strip()
    scoreList = line.split(",")
    scoreList = [int(i) for i in scoreList]
    finalScore = scoreList.pop()
    
    # Calculate score of the games
    g = Game()
    for roll in scoreList:
        g.roll(roll)
    score = g.score()
    print("The score of the game should be {}, the given score is {}".format(score, finalScore))
    
    # Check to see if the Scores match
    if score == finalScore:
        print("Congratulations! This score was correct.")
    else:
        print("Go back to math class!")