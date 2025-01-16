from itertools import combinations
import sys 
input = sys.stdin.readline
list1 = [i for i in range(2,119)]
for i in range(len(list1)):
    j = i
    while j < len(list1):
        if(list1[j] % list1[i] == 0 and list1[j] != list1[i]):
            list1.remove(list1[j])
        j += 1
set1 = set()
for i in range(len(list1)):
    set1.add(list1[i] * 2)
combi = list(combinations(list1,2))
for i in range(len(combi)):
    set1.add(sum(combi[i]))
n = int(input())
for i in range(n):
    a = int(input())
    if(a in set1):
        print("Yes")
    else:
        print("No")