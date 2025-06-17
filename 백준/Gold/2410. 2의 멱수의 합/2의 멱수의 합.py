n = int(input())
list1 = [0 for _ in range(n + 1)]
list1[1] = 1
a = 1000000000
for i in range(2,n + 1):
    if(i % 2 == 1):
        list1[i] = list1[i - 1]
    else:
        list1[i] = (list1[i - 1] % a + list1[i // 2] % a) % a
print(list1[n])