t = int(input())
list1 = []
while t >= 9:
    list1.append(t % 9)
    t //= 9
list1.append(t % 9)
list1.reverse()
for i in range(len(list1)):
    print(list1[i], end = "")