list1 = list(map(int,input().split()))
list1.remove(max(list1))
list1.remove(min(list1))
print(list1[0])