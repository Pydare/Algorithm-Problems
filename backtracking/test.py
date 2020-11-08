
value = 0
li = []
 
def recuision(n):
    #global value,li
    #Total number of records
    value += n
         #List records what numbers
    li.append(n)
         #Or change to this sentence li = [n], record the number of the last recursive process
    if(n == 1):
        return 1
    else:
        return n * recuision(n-1)
print(recuision(4))
 
