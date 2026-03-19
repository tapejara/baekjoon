from collections import deque
n, m = map(int,input().split())
list1 = list(map(int,input().split()))
dq = deque([i for i in range(1, n + 1)])
answer = 0
for i in range(m):
    if(dq.index(list1[i]) > len(dq) // 2):
        for j in range(len(dq) - dq.index(list1[i])):
            x = dq.pop()
            dq.appendleft(x)
            answer += 1
        dq.popleft()
    else:
        for j in range(dq.index(list1[i])):
            x = dq.popleft()
            dq.append(x)
            answer += 1
        dq.popleft()
print(answer)