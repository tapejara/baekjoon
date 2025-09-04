n = int(input())
list1 = []
list2 = []
for _ in range(n):
    a, b = map(int,input().split())
    list1.append(a - b)
if(n % 2 == 1):
    print(1)
else:
    list1.sort(reverse=True)
    for i in range(1, n):
        list2.append(list1[i - 1] - list1[i])
    print(abs(list2[(n - 1) // 2]) + 1)