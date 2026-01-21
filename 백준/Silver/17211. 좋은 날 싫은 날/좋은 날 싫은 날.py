n, c = map(int,input().split())
list1 = list(map(float,input().split()))
list2 = [[0,0]]
if(c == 0):
    list2[0][0] = 1
else:
    list2[0][1] = 1
for _ in range(n):
    temp = [0,0]
    temp[0] = list2[-1][0] * list1[0] + list2[-1][1] * list1[2]
    temp[1] = list2[-1][0] * list1[1] + list2[-1][1] * list1[3]
    list2.append(temp)
print(round(1000 * list2[-1][0]), round(1000 * list2[-1][1]))