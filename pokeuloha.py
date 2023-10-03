import json
fr = open('druhpoke.txt')
data = json.load(fr)
data1 = {}

for j,i in data.items():
    for x,y in i.items():
        if j == "super effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],2)
            data1[x] = data1.get(x,slov)
        if j == "normal effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],1)
            data1[x].update(slov)
        if j == "not very effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],0.5)
            data1[x].update(slov)
        if j == "no effect":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],0)
            data1[x].update(slov)

def attack(pt,dt,zoznam):
    zoznam = zoznam.strip().split(",")
    utok_pt = 0
    prvy_tim = [i.strip().split(" ") for i in zoznam[:pt]]
    druhy_tim = [i.strip().split(" ") for i in zoznam[pt:]]
    utok_dt = 0
    for i in prvy_tim:
        for j in druhy_tim:
            if len(i) == 1:
                if len(j) == 1:
                    utok_pt += data1[i[0]][j[0]]
                if len(j) == 2:
                    utok_pt += data1[i[0]][j[0]] * data1[i[0]][j[1]]
            if len(i) == 2:
                if len(j) == 1:
                    x = max(data1[i[0]][j[0]],data1[i[1]][j[0]])
                    utok_pt += x
                if len(j) == 2:
                    x = max(data1[i[0]][j[0]]*data1[i[0]][j[1]],data1[i[1]][j[0]]*data1[i[1]][j[1]])
                    utok_pt += x
    for i in druhy_tim:
        for j in prvy_tim:
            if len(i) == 1:
                if len(j) == 1:
                    utok_dt += data1[i[0]][j[0]]
                if len(j) == 2:
                    utok_dt += data1[i[0]][j[0]] * data1[i[0]][j[1]]
            if len(i) == 2:
                if len(j) == 1:
                    x = max(data1[i[0]][j[0]], data1[i[1]][j[0]])
                    utok_dt += x
                if len(j) == 2:
                    x = max(data1[i[0]][j[0]] * data1[i[0]][j[1]], data1[i[1]][j[0]] * data1[i[1]][j[1]])
                    utok_dt += x
    vys = ""
    utok_pt = round(utok_pt,1)
    utok_dt = round(utok_dt,1)
    if utok_pt > utok_dt:
        vys = "ME"
    elif utok_dt > utok_pt:
        vys = "FOE"
    elif utok_pt == utok_dt:
        vys = "EQUAL"
    return(utok_pt,utok_dt,vys)

print(attack(2,2,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))