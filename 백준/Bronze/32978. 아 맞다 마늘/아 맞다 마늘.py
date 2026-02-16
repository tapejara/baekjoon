n = int(input())
list1 = list(input().split())
list2 = list(input().split())
for c in list2:
    list1.remove(c)
print(list1[-1])