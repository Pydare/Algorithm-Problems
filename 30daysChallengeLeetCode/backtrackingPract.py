def diceRolls(dice):

    def diceHelper(dice,chosen):
        if dice == 0:
            #base case
            print(chosen)
        else:
            for die in range(6):
                #choose
                chosen.append(die)
                #explore
                diceHelper(dice-1,chosen)
                #unchose
                chosen.pop()
                                
    #dice = [i for i in range(dice)]
    diceHelper(dice,[])

print(diceRolls(3))