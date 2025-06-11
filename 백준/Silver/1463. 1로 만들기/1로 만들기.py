from collections import deque
n = int(input())
temp = deque([(n,0)])
while temp:
    a, b = temp.popleft()
    if(a == 1):
        print(b)
        break
    if(a % 3 == 0):
        temp.append((a // 3, b + 1))
        if(a // 3 == 1):
            print(b + 1)
            break
    if(a % 2 == 0):
        temp.append((a // 2, b + 1))
        if(a // 2 == 1):
            print(b + 1)
            break
    temp.append((a - 1, b + 1))
    if(a - 1 == 1):
        print(b + 1)
        break