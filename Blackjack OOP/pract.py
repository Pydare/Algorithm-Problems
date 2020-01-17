from functools import reduce
import string
def word_lengths(phrase):
    print(list(map(lambda phrase: len(phrase),phrase.split())))
    
#word_lengths('How long are the words in this phrase')
bad = word_lengths
bad('How long are the words in this phrase')

def digits_to_num(digits):
    return print(reduce(lambda x,y: x*10+y,list(digits)))

#digits_to_num([3,4,3,2,1])

l = ['hello','at','cat','dog','ham','hi','go','to','heart']
def filter_words(word_list,letter):
    print(list(filter(lambda word_list: word_list.startswith(letter),l)))

#filter_words(l,'h')

def concatenate(L1,L2,connector):
     return [(L1+connector+L2) for L1,L2 in zip(L1,L2)]

#concatenate(['A','B'],['a','b'],'-')

def d_list(L):
    print(dict([(i,num) for num,i in enumerate(L)]))

#d_list(['a','b','c'])

def count_match_index(L):
    print(len([count for count,i in enumerate(L) if count == i]))

#count_match_index([0,2,2,1,5,5,6,10])

#function to check for prime number from 10 to 20
# for num in range(10,20):
#     for i in range(2,num):
#        if num%i == 0:
#            print(num,' is not a prime number')
#            break
#     else:
#         print(num,' is a prime nummer')

def new_decorator(func):

    def wrap_func():
        print('This code executes before the func')
        func()
        print('This code executes after the func')
    return wrap_func

def func_needs_decorator():
    print('This function needs a decorator')

#func_needs_decorator = new_decorator(func_needs_decorator)


#algorithm to determine if a string has all unique characters
def unique(s):
    for letters in s:
        if s.count(letters) > 1:
            print(False)
            break
        else:
             print(True)
             break

#unique('bolo')

def uniques(s):
    print(len(set(s)) == len(s))

uniques('bark')




