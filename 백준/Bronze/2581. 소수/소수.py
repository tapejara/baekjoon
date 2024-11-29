a = int(input())
b = int(input())
list1 = []
for i in range(a,b + 1):
    c = 0
    for j in range(1,i + 1):
        if(i % j == 0):
            c += 1
    if(c == 2):
        list1.append(i)
if(len(list1) == 0):
    print(-1)
else:
    d = sum(list1)
    print(d)
    print(list1[0])