def minwindow(s,t):
    l = []
    for i in range(len(s)):
        if s[i] in t:
            l.append(i)
    gl = [l[i:i+3] for i in range(0,len(l),3)]
    range_list = [gl[i][2]-gl[i][0] for i in range(len(gl))]
    min_index = range_list.index(min(range_list))
    string_output = s[gl[min_index][0]:gl[min_index][2]+1]

    print(string_output)

minwindow("ADOBECODEBANC","ABC")