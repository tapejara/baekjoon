n = int(input())
list1 = [1]
i = 2
while list1[-1] < n:
    list1.append(i ** 2)
    i += 1
list2 = [[], [1]]
for j in range(2, n + 1):
    list3 = []
    for element in list1:
        if(j < element):
            break
        list3.append(list2[j - element] + [element])
    list3.sort(key = len)
    list2.append(list3[0])
print(len(list2[n]))