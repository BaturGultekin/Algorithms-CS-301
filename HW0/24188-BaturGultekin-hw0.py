
Teams = ['Lakers','Warriors','Celtics']
Players = ['LeBron','Curry','Kyrie']

Pteams = {'Lakers':['LeBron', 'Curry','Kyrie'],
            'Warriors':['Curry','LeBron','Kyrie'],
            'Celtics':['LeBron','Curry','Kyrie']
            }

Pplayers = {'LeBron':['Lakers','Warriors','Celtics'],
            'Curry':['Warriors', 'Lakers','Celtics'],
            'Kyrie':['Lakers', 'Warriors','Celtics']
            }

for i in Pteams:
    Pteams[i].reverse()

for i in Pplayers:
    Pplayers[i].reverse()

Contracts = {}
teamsWithFreeContrats = list (Teams)
numOfContracts = len (Teams)

while teamsWithFreeContrats:
    T = teamsWithFreeContrats.pop()
    P = Pteams[T].pop()
    if P not in Contracts: 
        Contracts[P]=T
    else:
        pickedTeam= Contracts[P]
        if Pplayers[P].index(T) > Pplayers[P].index(pickedTeam):
            Contracts[P] = T
            teamsWithFreeContrats.append(pickedTeam)
        else:
            teamsWithFreeContrats.append(T)

print (Contracts)