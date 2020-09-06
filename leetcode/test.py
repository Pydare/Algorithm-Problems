S = "abbcccddddaaaaa"
r = zip(*[(k,len(list(grp))) for k,grp in itertools.groupby(S)])
print(list(r))