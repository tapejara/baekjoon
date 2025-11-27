n , m = map(int,input().split())
list1 = [i for i in input()]
list2 = ["A", "E", "I", "O", "U"]
answer = []
for i in range(n - 1, -1, -1):
    if(len(answer) < 1 and (list1[i] not in list2)):
        answer.append(list1[i])
    elif(0 < len(answer) < 3 and list1[i] == "A"):
        answer.append(list1[i])
    elif(2 < len(answer) < m):
        answer.append(list1[i])
answer.reverse()
if(len(answer) == m):
    print("YES")
    for i in range(m):
        print(answer[i], end = "")
else:
    print("NO")