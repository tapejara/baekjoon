from collections import deque
n, k, m = map(int,input().split())
deq = deque([i for i in range(1, n + 1)])
answer = deque([])
countM = 0
direction = 1
for i in range(n):
    if(direction == 1):
        if(k <= n):
            for j in range(k - 1):
                deq.append(deq.popleft())
            answer.append(deq.popleft())
            countM += 1
        elif(k > n):
            for j in range(k % n - 1):
                deq.append(deq.popleft())
            answer.append(deq.popleft())
            countM += 1
    elif(direction == -1):
        if(k <= n):
            for j in range(k - 1):
                deq.appendleft(deq.pop())
            answer.append(deq.pop())
            countM += 1
        elif(k > n):
            for j in range(k % n - 1):
                deq.appendleft(deq.pop())
            answer.append(deq.pop())
            countM += 1
    if(countM == m): 
        countM = 0
        direction *= -1
for element in answer:
    print(element)