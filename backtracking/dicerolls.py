'''
Give n number of dice, print all possible combinations of the dice
eg, n=2: 11,12,13,14,15,16,21,22,23,24,25,26,31,32,33,34,35,36
'''

def dice_helper(dice,tracker):
    #base case: when dice is 0, we're done exploring
    if dice == 0:
        print(tracker)
    else:
        for i in range(1,7):
            #choose
            tracker.append(i)
            #explore
            dice_helper(dice-1,tracker)
            #unchoose
            tracker.pop()


def diceroll_maain(dice):
    tracker = []
    dice_helper(dice,tracker)

print(diceroll_maain(3))