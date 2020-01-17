def pushDominoes(dominoes):
    dominoes = [i for i in dominoes]
    i = 0
    while i < (len(dominoes)):
        if dominoes[i] == 'R' and i != len(dominoes)-1:
            dominoes[i+1] = 'R'
            i += 1
        if dominoes[i] == 'L' and i != 0:
            dominoes[i-1] = 'L'
            i += 1
        if dominoes[i] == 'R' and (i) < len(dominoes)-1 and dominoes[i+2] == 'L':
            dominoes[i+1] == '.'
            i += 2
        i += 1
    return ''.join(dominoes)


print(pushDominoes(".L.R...LR..L.."))