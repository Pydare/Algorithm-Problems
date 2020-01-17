def passphraseStrength(s):
    s = s.split()
    s_check = list(set(s))
    if len(s) == len(s_check):
        return 'strong'
    else:
        return 'weak'

print(passphraseStrength('aa bb cc dd ee dd'))

