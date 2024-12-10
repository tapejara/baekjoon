a, b = map(int,input().split())
list1 = []
for _ in  range(b):
    e = 0
    list1.append(e)
for i in range(a):
    c = input()
    d = c.replace(" ", "")
    for j in range(b):
        if(d[j] == "1"):
            list1[j] += 1
for k in range(b):
    print(list1.index(max(list1)) + 1, end=" ")
    list1[list1.index(max(list1))] = 0