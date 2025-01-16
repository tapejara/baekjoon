import sys 
input = sys.stdin.readline
n, m = map(int,input().split())
s = ""
distance = 0
list1 = [[0,0,0,0] for _ in range(m)]
for _ in range(n):
    dna = input()
    for j in range(m):
        if(dna[j] == "A"):
            list1[j][0] += 1
        elif(dna[j] == "C"):
            list1[j][1] += 1
        elif(dna[j] == "G"):
            list1[j][2] += 1
        else:
            list1[j][3] += 1 
for i in range(m):
    if(max(list1[i]) == list1[i][0]):
        s += "A"
        list1[i].remove(max(list1[i]))
    elif(max(list1[i]) == list1[i][1]):
        s += "C"
        list1[i].remove(max(list1[i]))
    elif(max(list1[i]) == list1[i][2]):
        s += "G"
        list1[i].remove(max(list1[i]))
    else:
        s += "T"
        list1[i].remove(max(list1[i]))
for i in range(m):
    distance += sum(list1[i])
print(s)
print(distance)