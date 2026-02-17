n = int(input())
list1 = [0, 1, 1]
for i in range(3, n + 1):
    list1.append(list1[-1] + list1[-2])
print(list1[-1])