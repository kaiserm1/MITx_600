
# Exercise 4
import random

precision = 0.002
bucket = ['r', 'r', 'r', 'g', 'g', 'g']


def pick_balls_from_bucket(bucket, numBalls=3):
    """ Pick a ball from a bucket n-times, without replacing the balls.
        bucket = list of balls in a bucket
        numBalls = number of balls to pull from bucket
        returns: list of balls picked
    """
    return random.sample(bucket, k=numBalls)


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    num_same_color = 0
    for t in range(numTrials):
        pick = pick_balls_from_bucket(bucket, numBalls=3)
        if len(set(pick)) == 1:
            num_same_color += 1
    return num_same_color / numTrials


print(noReplacementSimulation(100000))
