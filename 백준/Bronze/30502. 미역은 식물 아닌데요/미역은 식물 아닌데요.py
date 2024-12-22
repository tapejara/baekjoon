n, m = map(int,input().split())
list1 = []
list2 = []
for i in range(n + 1):
    list1.append(0)
for _ in range(m):
    a,b,c = input().split()
    if([a,b,c] in list2):
        continue
    list2.append([a,b,c])
    a1 = int(a)
    c1 = int(c)
    if(b == "P" and c1 == 1):
        list1[a1] += 1
    elif(b == "M" and c1 == 0):
        list1[a1] += 1 
    elif(b == "P" and c1 == 0):
        list1[a1] -= 2
    elif(b == "M" and c1 == 1):
        list1[a1] -= 2
d = 0
e = 0
for element in list1:
    if(element >= 2):
        d += 1
    elif(element < 0):
        e += 1
print(d, n - e)