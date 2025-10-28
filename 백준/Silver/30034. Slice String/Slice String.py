n = int(input())
set1 = set()
a = list(input().split())
for i in range(n):
    set1.add(a[i])
m = int(input())
b = list(input().split())
for i in range(m):
    set1.add(b[i])
k = int(input())
c = list(input().split())
for i in range(k):
    if(c[i] in set1):
        set1.remove(c[i])
s = int(input())
t = input()
flag = False
answer = ""
for i in range(s):
    if(t[i] in set1 or t[i] == " "):
        if(flag == False):
            answer += "\n"
            flag = True
        else:
            continue
    else:
        answer += t[i]
        flag = False
print(answer.strip())