def sub_lists(v):
    chosen = []
    sublists_helper(v,chosen)

def sublists_helper(v,chosen):
    if not v:
        print(chosen)
    else:
        #2 choices to explore, subset w 1st one and the other w/o it
        first = v[0]
        v.pop(0)

        #chose/explore with
        chosen.append(first)
        sublists_helper(v, chosen)

        #choose/explore without
        chosen.pop()
        sublists_helper(v,chosen)

        #unchoose
        v.insert(0,first)

print(sub_lists(['Jane','Bob',"Matt",'Sarah']))