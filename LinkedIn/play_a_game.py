'''
This game is called "Patience". 
When the player start the game, you will tell him to wait a random amount of time [2s-4s] then press Enter!
the player presses Enter to start waiting
and then, when he feels like the timer has finished, he should press Enter again!
then you are supposed to tell him if his response was slower, faster, or at the exact time!
'''

import time
import random

def waiting_game():
    target = random.randint(2,4)
    print('\nYour target time is {} seconds'.format(target))
    input(' ---Press Enter to Begin--- ')
    # Getting the current time in seconds, very precised!
    start = time.perf_counter()
    input('\n...Press Enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start
    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))


waiting_game()