n, k = map(int,input().split())
list1 = [i for i in range(1, n + 1)]
answer = []
a = 0
for _ in range(n * k):
    if(list1.count("@") == n):
        break
    for i in range(len(list1)):
        if(list1[i] != "@"):
            a += 1
        if(a == k):
            answer.append(list1[i])
            list1[i] = "@"
            a = 0
print("<",end = "")
for i in range(len(answer) - 1):
    print(f"{answer[i]}, ", end = "")
print(f"{answer[-1]}>")