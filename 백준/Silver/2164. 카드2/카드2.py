from collections import deque
a = int(input())
list1 = deque([i for i in range(1,a + 1)])
for _ in range(a):
    if(len(list1) > 1):
        list1.popleft()
        list1.append(list1.popleft())
    else:
        break
print(list1[0])