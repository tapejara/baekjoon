from collections import deque
n, k = map(int,input().split()) 
deq = deque([i for i in range(1, n + 1)])
for _ in range(len(deq)):
    if(len(deq) >= k):
        deq.append(deq.popleft())
        for i in range(k - 1):
            deq.popleft()
    else:
        print(deq.popleft())
        break