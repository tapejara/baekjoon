list1 = []
for i in range(1, 9):
    n = int(input())
    list1.append((n, i))
list1.sort(reverse=True)
answer1 = 0
answer2 = []
for i in range(5):
    answer1 += list1[i][0]
    answer2.append(list1[i][1])
answer2.sort()
print(answer1)
for i in range(5):
    print(answer2[i], end= " ")