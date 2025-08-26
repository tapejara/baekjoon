s, p = map(int,input().split())
list1 = [c for c in input()]
a, c, g, t = map(int,input().split())
answer = 0
flag = [list1[0:p].count("A"), list1[0:p].count("C"), list1[0:p].count("G"), list1[0:p].count("T")]
if(flag[0] >= a and flag[1] >= c and flag[2] >= g and flag[3] >= t):
    answer += 1
for i in range(p,s):
    if(list1[i - p] == "A"):
        flag[0] -= 1
    elif(list1[i - p] == "C"):
        flag[1] -= 1
    elif(list1[i - p] == "G"):
        flag[2] -= 1
    elif(list1[i - p] == "T"):
        flag[3] -= 1
    if(list1[i] == "A"):
        flag[0] += 1
    elif(list1[i] == "C"):
        flag[1] += 1
    elif(list1[i] == "G"):
        flag[2] += 1
    elif(list1[i] == "T"):
        flag[3] += 1
    if(flag[0] >= a and flag[1] >= c and flag[2] >= g and flag[3] >= t):
        answer += 1
print(answer)