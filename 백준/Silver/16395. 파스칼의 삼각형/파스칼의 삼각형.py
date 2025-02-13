n, k = map(int,input().split())
list1 = [[], [1], [1, 1]]
for i in range(3, n + 1):
    list2 = [1]
    for j in range(1, i - 1):
        list2.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list2.append(1)
    list1.append(list2)
print(list1[n][k - 1])