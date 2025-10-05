n = int(input())
list1 = []
for _ in range(n):
    a, b = map(int,input().split())
    if(a <= b):
        list1.append(b)
if(list1):
    print(min(list1))
else:
    print(-1)