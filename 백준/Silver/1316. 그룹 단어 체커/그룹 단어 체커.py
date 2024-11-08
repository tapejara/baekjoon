a = int(input())
answer = 0
for _ in range(a):
    b = input()
    list1 = []
    for i in range(len(b)):
        list1.append(b[i])
        if(i >= 1 and list1.count(b[i]) >= 2 and not list1[i-1] == list1[i]):
            break
        if(len(list1) == len(b)):
            answer += 1
print(answer)