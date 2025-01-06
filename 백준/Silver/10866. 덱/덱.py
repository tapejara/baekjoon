import sys
input = sys.stdin.readline
from collections import deque
deq = deque([])
a = int(input())
for i in range(a):
    b = input()
    if("push_front" in b):
        c, d = b.split()
        deq.appendleft(int(d))
    elif("push_back" in b):
        c, d = b.split()
        deq.append(int(d))
    elif(b == "pop_front\n"):
        if(len(deq) != 0):
            print(deq.popleft())
        else:
            print(-1)
    elif(b == "pop_back\n"):
        if(len(deq) != 0):
            print(deq.pop())
        else:
            print(-1)
    elif(b == "size\n"):
        print(len(deq))
    elif(b == "empty\n"):
        if(len(deq) == 0):
            print(1)
        else:
            print(0)
    elif(b == "front\n"):
        if(len(deq) == 0):
            print(-1)
        else:
            print(deq[0])
    elif(b == "back\n"):
        if(len(deq) == 0):
            print(-1)
        else:
            print(deq[-1])