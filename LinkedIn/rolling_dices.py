''' 
For this challenge, we need to write a function that display the probabilities of rolling multiple dices at the
time, these probabilities aren't calculated mathematically, they are calculated using a set, in other words,
we will be experiencing things, that calculating the probabilities :c
*dice : means that our function accepts multiple arguments.
'''
from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):  
    counts = Counter()
    # We first do our 1000000 trials, and for each trial, we increment counts[res] by one, sounds pretty intuitive right ?
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1
    
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))
        
# Normally distributed!
roll_dice(4,6,6)
roll_dice(4,6,6,20)
