n, m = map(int,input().split())
answer1 = 1
answer2 = 0
for i in range(max(n,m), 1, -1):
    if(n % i == 0 and m % i == 0):
        answer1 = i
        break
list1 = []
list2 = []
for i in range(1,max(n,m) + 1):
    list1.append(n * i)
    list2.append(m * i)
    if(n * i in list2):
        answer2 = n * i
        break
    elif(m * i in list1):
        answer2 = m * i
        break
print(answer1)
print(answer2)