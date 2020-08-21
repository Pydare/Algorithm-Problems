def fully_justify(words,maxwidth):
    res, curr, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(curr) > maxwidth:
            for i in range(maxwidth - num_of_letters):
                curr[i%(len(curr)-1 or 1)] += ' '
            res.append(''.join(curr))
            curr, num_of_letters = [], 0
        curr += [w]
        num_of_letters += len(w)
    return res + [' '.join(curr).ljust(maxwidth)]