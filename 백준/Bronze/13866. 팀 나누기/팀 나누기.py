list1 = list(map(int,input().split()))
a = 0
a += max(list1) + min(list1)
list1.remove(max(list1))
list1.remove(min(list1))
b = sum(list1)
print(abs(a - b))