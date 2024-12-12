a, b = map(int,input().split())
list1 = []
f = 0
for _ in range(a):
    c = input()
    d = ""
    for element in c:
        d += element + element
    list1.append(d)
for i in range(a):
    e = input()
    if(list1[i] == e):
        f += 1
    else:
        print("Not Eyfa")
        break
if(a == f):
    print("Eyfa")