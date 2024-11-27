a,b = map(int,input().split())
list1 = []
for i in range(1,a + 1):
    if(a % i == 0):
        list1.append(i)
if(len(list1) < b):
    print(0)
else:
    print(list1[b - 1])