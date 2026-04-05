import sys
input = sys.stdin.readline
k, l = map(int,input().split())
list1 = [input().strip() for _ in range(l)]
list2 = []
set1 = set()
list1.reverse()
for i in range(l):
    if(list1[i] not in set1):
        set1.add(list1[i])
        list2.append(list1[i])
    else:
        continue
list2.reverse()
for i in range(min(len(list2),k)):
    print(list2[i])