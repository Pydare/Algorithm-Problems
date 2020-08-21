t = 'abbccs'
d = {}
d = {x: d.get(x, 1) + 1 for x in t}
print(d)