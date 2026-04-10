from itertools import permutations
import sys
input = sys.stdin.readline
list1 = [0]
for i in range(1,9):
    for t in permutations([1,2,3,4,5,6,7,8,9,0], i):
        a = ""
        for c in t:
            if(len(a) == 0 and c == 0):
                break
            a += str(c)
        if(a):
            list1.append(int(a))
list1.sort()
while True:
    n = int(input())
    if(n == 0):
        exit()
    print(list1[n])