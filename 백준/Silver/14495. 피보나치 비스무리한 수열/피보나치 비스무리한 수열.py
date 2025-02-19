n = int(input())
list1 = [1, 1, 1]
for i in range(3, n):
    list1.append(list1[i - 1] + list1[i - 3])
print(list1[n - 1])