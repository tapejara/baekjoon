a = int(input())
list1 = []
list2 = []
for i in range(a):
    b,c = map(int,input().split())
    list1.append(b)
    list2.append(c)
print((max(list1) - min(list1)) * (max(list2) - min(list2)))