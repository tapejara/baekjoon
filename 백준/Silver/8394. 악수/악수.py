n = int(input())
list1 = [1, 2]
for i in range(2, n):
    list2 = list(str(list1[i - 1] + list1[i - 2]))
    list1.append(int(list2[-1]))
print(list1[n - 1])