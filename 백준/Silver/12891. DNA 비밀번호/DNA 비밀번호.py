s, p = map(int,input().split())
dna = input()
list1= []
for c in dna:
    if(c == "A"):
        list1.append(0)
    elif(c == "C"):
        list1.append(1)
    elif(c == "G"):
        list1.append(2)
    else:
        list1.append(3)
a, c, g, t = map(int,input().split())
answer = 0
flag = [list1[0:p].count(0), list1[0:p].count(1), list1[0:p].count(2), list1[0:p].count(3)]
for i in range(p,s + 1):
    if(flag[0] >= a and flag[1] >= c and flag[2] >= g and flag[3] >= t):
        answer += 1
    if(i != s):
        flag[list1[i - p]] -= 1
        flag[list1[i]] += 1
print(answer)