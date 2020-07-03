def dice_helper(dice,tracker,desired_sum,sum_so_far):
    #base case: when dice is 0, we're done exploring
    if dice == 0:
        if sum_so_far == desired_sum:
            print(tracker)
    else:
        for i in range(1,7):
            #choose
            if sum_so_far+i+1*(dice-1) <= desired_sum and sum_so_far+i+6*(dice-1)>=desired_sum:
                tracker.append(i)
                #explore
                dice_helper(dice-1,tracker,desired_sum,sum_so_far+i)
                #unchoose
                tracker.pop()


def diceroll_maain(dice,desired_sum,sum_so_far):
    tracker = []
    dice_helper(dice,tracker,desired_sum,sum_so_far)

print(diceroll_maain(3,7,0))