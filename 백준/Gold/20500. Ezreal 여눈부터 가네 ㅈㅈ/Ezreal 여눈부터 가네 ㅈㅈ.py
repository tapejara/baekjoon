n = int(input())
a = 1000000007
list1 = [0, 0, 1, 1]
for i in range(4, n + 1):
    list1.append(((list1[i - 2] * 2) % a + list1[i - 1] % a) % a)
print(list1[n])