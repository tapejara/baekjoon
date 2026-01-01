n = int(input())
l = 1
list1 = [(0, 0), (1, 1)]
while list1[-1][1] <= 10**9:
    list1.append((list1[-1][0] + 4 * l, list1[-1][1] + list1[-1][0] + 4 * l))
    l += 1
for i in range(len(list1)):
    if(n < list1[i][1]):
        print(i - 1)
        exit()