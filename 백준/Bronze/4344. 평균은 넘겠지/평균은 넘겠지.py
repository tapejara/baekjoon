n = int(input())
for _ in range(n):
    list1 = list(map(int,input().split()))
    a = sum(list1[1:]) / list1[0]
    count = 0
    for i in range(1,len(list1)):
        if(list1[i] > a):
            count += 1
    print(f"{round(count / list1[0] * 100, 3)}%")