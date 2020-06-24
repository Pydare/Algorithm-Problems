def reverse_words(s):
    return ' '.join(reversed(s.split()),)

res = reverse_words('I dont love you')
print(res)