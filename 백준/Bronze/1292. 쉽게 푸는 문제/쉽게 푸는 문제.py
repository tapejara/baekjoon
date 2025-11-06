start, end = map(int,input().split())
list1 = []
for i in range(1,47):
    for j in range(i):
        list1.append(i)
print(sum(list1[start - 1 : end]))