a = int(input())
list1 = list(map(int,input().split()))
b = max(list1)
c = 0
for elemnt in list1:
    c += elemnt/b*100
print(c/a)