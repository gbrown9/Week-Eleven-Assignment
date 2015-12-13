# Basic Structure for a Random Walk simulation
# Dan Neumann
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here

def main():
    printHeader()
    for n in range(100,1000,10):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("You flip a coin. If it comes up heads, you take a step forward; tails means to take a step backward.")

def getRandomWalk(steps):
    # Calculate a random walk of given steps
    
    location = 0
     
    coinFlip = random.randint(0,1) # Calculate random number for direction 
    if coinFlip == 0:
        location += 1
    elif coinFlip == 1:
        location -= 1
    return location # replace with actual average

if __name__ == "__main__":
    main()