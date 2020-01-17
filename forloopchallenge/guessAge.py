def guess_the_age():
    number_of_trials = 3
    print('Guess my age')
    age = int(input())
    for i in range(number_of_trials-1):
        if age == 20:
            print('YOURE RIGHT!')
            break
        elif age>10 and age<20:
            print('Age is more!\n Guess again')
            age = int(input())
            number_of_trials-=1
            if number_of_trials == 0:
                print('YOU LOOSE!')
        elif age>30 and age<40:
            print('Age is less less!\n Guess again')
            age = int(input())
            number_of_trials-= 1 
            if number_of_trials == 0:
                print('YOU LOOSE!')
        elif age>20 and age<25:
            print('Age is close!\n Guess again')
            age = int(input())
            number_of_trials-=1
            if number_of_trials == 0:
                print('YOU LOOSE!')
        else:
            print('Youre totally out of range!\nGuess again')
            age = int(input())
            number_of_trials-=1
            if number_of_trials == 0:
                print('YOU LOOSE!')
    


guess_the_age()
