""""
Given a primitive calculator that can perform the following three operations with the current number x: multiply x by 2, 
multiply x by 3, or add 1 to x.Compute the minimum number of operations needed to obtain the number n starting from the number 1.
Also, print out the sequence of numbers to get to n.

Input1: n = 5
Output1: 3
        1,2,4,5
Input2: n = 10
Output2: 1,3,9,10

Input3: n = 96234
Output3: 1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234

"""

# Uses python3
import sys

def min_ops(n):
    result = []
    for i in range(0, n+1):
        result.append(0)
    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 2 == 0:
            min2 = result[int(i/2)]
        if i % 3 == 0:
            min3 = result[int(i/3)]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1

    return result

def construct_min_list(n, ops):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0: 
            n = n // 3
        elif n % 2 == 0:
            if ops[n-1] < ops[n//2]:
                n = n-1
            else:
                n = n // 2
        elif n % 3 == 0: 
            if ops[n-1] < ops[n//3]:
                n = n-1
            else:
                n = n // 3
    return reversed(sequence)

def optimal_sequence(n):
    if n == 1:
        return [1]
    ops = min_ops(n)
    return construct_min_list(n, ops)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')