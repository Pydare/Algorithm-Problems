import re
def getEventsOrder(team1, team2, events1, events2):
    #either add the team name to all
    #or print the team name at the end with all of them
    e1 = [team1+' '+i for i in events1]
    e2 = [team2+' '+i for i in events2]
    all_teams = e1 + e2

    def grp(pat, txt): 
        r = re.search(pat, txt)
        return r.group(0) if r else '&'

    all_teams.sort(key=lambda l: grp("\d\d", l))
    return(all_teams)


e1 = ['inmuucz jzbkica 70 Y','ton wfnt 10 S inmuucz jzbkica','ecya kqvqy 20 S fkfk fuiyb senmofw']
e2 = ['mysior pqfcz bxlnpn 49 G','mysior pqfcz bxlnpn 18 G','enc otagavd oevfg 68 Y']
print(getEventsOrder('nolh','uzrdrrc slcpx',e1,e2))
