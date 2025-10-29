n, m = map(int,input().split())
s = [i for i in input()]
c = s.copy()
c.sort()
list0 = [0 for _ in range(26)]
list1 = c[:m]
answer = []
for i in range(m):
    list0[ord(list1[i]) - 97] += 1
for i in range(n):
    if(list0[ord(s[i]) - 97] > 0):
        list0[ord(s[i]) - 97] -= 1
        continue
    else:
        answer.append(s[i])
for i in range(len(answer)):
    print(answer[i], end = "")