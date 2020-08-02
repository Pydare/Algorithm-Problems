titles = ['Baka to Test to Shoukanjuu','Baka to Test to Shoukanjuu Mini Anime','Baka to Test to Shoukanjuu Ni',
        'Baka to Test to Shoukanjuu Ni!: Mahou Hideyoshi Hideyoshi','Baka to Test to Shoukanjuu Specials',
        'Baka to Test to Shoukanjuu: Matsuri','Baka to Test to Shoukanjuu: Matsuri - Sentaku ni Yotte Tenkai ga Kawaru "LIPS Eizou"',
        'Gabriel DropOut','Gabriel DropOut Specials','Hajime no Ippo','Hajime no Ippo: Boxer no Kobushi','Hajime no Ippo: Champion Road',
        'Hajime no Ippo: New Challenger','Hajime no Ippo: Rising']

"""
return value --> Baka to Test to Shoukanjuu, Gabriel DropOut, Hajime no Ippo
"""
from collections import OrderedDict
def compare(s,t):
    len_s = len(s)
    if s == t[:len_s]:
        return True
    else:
        return False

def grouping(titles):
    d = OrderedDict()
    d[titles[0]] = []

    for i in range(1,len(titles)):
        target_key = list(d.keys())[-1]
        if compare(target_key,titles[i]):
            d[target_key].append(titles[i])
        else:
            d[titles[i]] = []
    return list(d.keys()) 

res = grouping(titles)
print(res)

def get_base_from_repitions(titles):

    title_lens = [len(title) for title in titles]
    min_index = title_lens.index(min(title_lens))

    base_word = titles[min_index]
    