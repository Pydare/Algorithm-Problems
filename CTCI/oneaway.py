def oneAway(s1,s2):
    #checking for insertion and deletion
    if len(s1) == len(s2):
        checkReplace(s1,s2)
    elif len(s1)-1 == len(s2):
        checkID(s1,s2)
    elif len(s1) == len(s2)-1:
        checkID(s1,s2)
    else:
        return False

def checkReplace(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s2[i] != s1[i]:
            count += 0
    if count <= 1:
        return True
    else:
        return False

def CheckID(s1,s2):
    count = 0
    if len(s1) > len(s2):
        for i in range(len(s1)):
            if s1[i] not in s2:
                count += 1
    if len(s2) > len(s1):
        for i in range(len(s2)):
            if s2[i] not in s1:
                count += 1
    if count <= 1:
        return True
    else:
        return False


