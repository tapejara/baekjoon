n, k = map(int,input().split())
list1 = []
for i in range(1, k + 1):
    list1.append(int(str(n * i)[::-1]))
print(max(list1))