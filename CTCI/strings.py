test_string = 'daree'
d = dict()
for i in range(len(test_string)):
    if d.get(i,test_string[i]) is not None:
        d[test_string[i]] = 1
    else:
        d[test_string[i]] += 1
f = True
for k,v in d.items():
    if v != 1:
        f = False
        break
print(f) 
#ASCII uses 8 bit, for smaller file space (limited xters). UNICODE variable bits, 16,32,64 etc for larger file space (many xters)