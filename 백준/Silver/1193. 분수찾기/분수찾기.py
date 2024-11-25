a = int(input())
b = 0
c = 1
for i in range(a):
    b += i
    if(a <= b):
        b -= a
        break
    c += 1
list1 = []
for i in range(1,c):
    list1.append([i,c - i])
if(c % 2 == 0):
    print(list1[b][0], "/" ,list1[b][1], sep='')
else:
    list1.reverse()
    print(list1[b][0], "/" ,list1[b][1], sep='')