n = int(input())
list1 = list(map(int,input().split()))
p = list1[0]
a = 1
for i in range(1, n):
    if(p <= list1[i]):
        a += 1
        p = list1[i]
    else:
        p = list1[i]
print(a)