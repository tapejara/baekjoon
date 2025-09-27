from collections import deque
n, k = map(int,input().split())
dist = [1e99 for _ in range(10 ** 5 + 1)]
dist[n] = 0
q = deque([n])
while q:
    current = q.popleft()
    if(2 * current <= 10**5 and dist[2*current] > dist[current]):
        dist[2*current] = dist[current]
        q.appendleft(2*current)
    if(current + 1 <= 10**5 and dist[current + 1] > dist[current] + 1):
        dist[current + 1] = dist[current] + 1
        q.append(current + 1)
    if(current - 1 >= 0 and dist[current - 1] > dist[current] + 1):
        dist[current - 1] = dist[current] + 1
        q.append(current - 1)
print(dist[k])