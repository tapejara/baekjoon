from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
def function(num,ab,array):
    for _ in range(num):
        a, b = map(str,input().split())
        c, d = map(int,a.split(":"))
        e, f = map(int,b.split(":"))
        start = c * 60 + d
        end = e * 60 + f + t
        array.append([start,end,ab])
for x in range(n):
    t = int(input())
    na, nb = map(int,input().split())
    list1 = []
    function(na,0,list1)
    function(nb,1,list1)
    answer_a = na
    answer_b = nb
    list1.sort()
    dq = deque(list1.copy())
    while dq:
        temp = dq.popleft()
        for i in range(len(list1)):
            if(temp[1] <= list1[i][0] and temp[2] != list1[i][2]):
                if(list1[i][2] == 0):
                    answer_a -= 1
                else:
                    answer_b -= 1
                list1.remove(list1[i])
                break
    print(f'Case #{x + 1}: {answer_a} {answer_b}')