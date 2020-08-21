def words_typing(sentence, rows, cols):
    
    s = ' '.join(sentence) + ' '
    start = 0

    for _ in range(rows):
        start += cols-1
        if s[start%len(s)] == ' ':
            start += 1
        elif s[(start+1)%len(s)] == ' ':
            start += 2
        else:
            while start > 0 and s[(start-1) % len(s)] != ' ':
                start -= 1

    return start/len(s)


"""
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

s = 'a bcd e ' len(s) = 8

start = 12
row=1

"""
