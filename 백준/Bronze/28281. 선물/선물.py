n, x = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = []
for i in range(1,len(list1)):
    list2.append((list1[i - 1] + list1[i]) * x)
print(min(list2))