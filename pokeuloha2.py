import json

with open('druhpoke.txt', 'r') as fr:
    data = json.load(fr)

data1 = {}
for j, i in data.items():
    for x, y in i.items():
        slov = {}
        for z in range(len(y)):
            if j == "super effective":
                slov[y[z]] = 2
            elif j == "normal effective":
                slov[y[z]] = 1
            elif j == "not very effective":
                slov[y[z]] = 0.5
            elif j == "no effect":
                slov[y[z]] = 0
        data1.setdefault(x, {}).update(slov)

def attack(pt, dt, zoznam):
    zoznam = zoznam.strip().split(",")
    utok_pt = 0
    prvy_tim = [i.strip().split(" ") for i in zoznam[:pt]]
    druhy_tim = [i.strip().split(" ") for i in zoznam[pt:]]
    utok_dt = 0

    for i in prvy_tim:
        for j in druhy_tim:
            utok_pt += max([data1[p1][p2] for p1 in i for p2 in j])

    for i in druhy_tim:
        for j in prvy_tim:
            utok_dt += max([data1[p1][p2] for p1 in i for p2 in j])

    utok_pt = round(utok_pt, 1)
    utok_dt = round(utok_dt, 1)

    if utok_pt > utok_dt:
        vys = "ME"
    elif utok_dt > utok_pt:
        vys = "FOE"
    else:
        vys = "EQUAL"

    return utok_pt, utok_dt, vys

result = attack(2, 2, "Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug")
print(result)