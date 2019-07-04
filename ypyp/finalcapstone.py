from math import pi
from math import e
from functools import reduce
import random
# def get_Number():
#     num = int(input('Enter your number of decimal places for the pi '))
#     return num
# x = get_Number()
# print(format(e,'.'+str(x)))
# print('%6.8f  for the 4 decimal places'%(pi))

#fibonnaci function
def fibon(n):
    a = 1
    b = 1
    L = []
    for numbers in range(n):
        a,b = b,a+b
        L.append(a)
    print(L)
#fibon(10)

#prime factors of all the numbers
def getPnums(n):
    for i in range(1,n):
        if n%i == 0:
            print(i, 'is a prime factor')
        else :
            print(i, 'is not a prime factor')
    
#getPnums(15)

#keep requesting for prime numbers
# def request():
#     r = 'y'
#     while r != 'n':
#         x = int(input('Enter a digit: '))
#         for numbers in range(2,int(x**0.5)-1):
#             if x%numbers == 0:
#                 print(x,'is not a prime number')
#                 break
#             else:
#                 print(x,'is a prime number')
#                 break
              
#         r = input('Do you want to continue?') 
            
# request()

#Cost of tile to cover W X H floor
# def cost_of_tile(price):
#     w = int(input('Please enter your value of width: '))
#     h = int(input('Please enter your value of height: '))
#     A = w*h
#     total_cost = price*A
#     print('Your total cost is %s'%(total_cost))
 

# cost_of_tile(50)

#factorial finder
def factorial(n):
   x = reduce(lambda x,y:x*y,range(1,n+1))
   print(x)

#factorial(4)

#NUMBER NAMES    
# def converter():
#     n = int(input('Enter the number to be named: '))
#     units = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
#     tens = {20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
#     hundreds = {100:'onehundred',200:'twohundred',300:'threehundred',400:'fourhundred',500:'fivehundred',600:'sixhundred',700:'sevenhundred',800:'eighthundred',900:'ninehundred'}
#     if n>=1 and n<20:
#         print(units[n])
#     elif n == 0:
#         print('zero')
#     elif n>=20 and n<100:
#         print(tens[n-n%10]+units[n%10])
#     elif n>=100 and n<1000:
#         print(hundreds[n-n%100]+'and'+tens[n%100-(n%100)%10]+units[(n%100)%10])

#RANDOM COIN FLIP RESULTS
# def coinflip():
#     outcomes = {0:'head',1:'tail'}
#     h = 0
#     t = 0
#     v = int(input('Enter how many times you want the coin flipped: '))
#     for i in range(v):
#         print(outcomes[random.randint(0,1)])
#         if outcomes[random.randint(0,1)] == 'head':
#             h += 1
#         elif outcomes[random.randint(0,1)] == 'tail':
#             t += 1
#     print('Total number of heads is',h,'Total number of tails is ',t)


#COLLECTIONS MODULE
def collector(L):
    d = {}
    for dkey in L:
        for dvalue in L:
            d[dkey] = L
            x = L.index(dvalue)
            x = d.values()
    return d

collector(['boy','girl','man','woman'])
  


