n = int(input())
list1 = [n for _ in range(n + 1)]
list1[1] = 0
for i in range(1,n):
    if(i + 1 < n + 1):
        list1[i + 1] = min(list1[i] + 1, list1[i + 1])
    if(i * 2 < n + 1):
        list1[i * 2] = min(list1[i] + 1, list1[i * 2])
    if(i * 3 < n + 1):
        list1[i * 3] = min(list1[i] + 1, list1[i * 3])
print(list1[n])