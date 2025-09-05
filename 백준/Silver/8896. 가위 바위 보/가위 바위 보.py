import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    winner = [i for i in range(n)]
    list1 = [input() for _ in range(n)]
    k = len(list1[0])
    for i in range(k):
        list2 = []
        for j in range(n):
            if(j in winner):
                list2.append(list1[j][i])
            else:
                list2.append(0)
        if(list2.count("R") > 0 and list2.count("S") > 0 and list2.count("P") > 0):
            continue
        elif(list2.count("R") > 0 and list2.count("S") > 0):
            for l in range(n):
                if(list2[l] == "S"):
                    winner.remove(l)
        elif(list2.count("P") > 0 and list2.count("R") > 0):
            for l in range(n):
                if(list2[l] == "R"):
                    winner.remove(l)
        elif(list2.count("S") > 0 and list2.count("P") > 0):
            for l in range(n):
                if(list2[l] == "P"):
                    winner.remove(l)
    if(len(winner) > 1):
        print(0)
    else:
        print(winner[0] + 1)