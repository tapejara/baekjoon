t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    list1 = [[i for i in range(1, n + 1)]]
    for i in range(1, k + 1):
        list2 = []
        list1.append(list2)
        for j in range(n):
            list1[i].append(sum(list1[i - 1][:j + 1]))
    print(list1[k][n - 1])