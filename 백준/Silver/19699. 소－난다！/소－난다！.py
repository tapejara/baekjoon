from itertools import combinations
combi = combinations
prime = set(i for i in range(2, 9001))
for i in range(2, 9001):
    if(i in prime):
        for j in range(i * 2, 9001, i):
            prime.discard(j)
n, m = map(int,input().split())
h = list(map(int,input().split()))
list1 = list(combi(h, m))
set1 = set()
for element in list1:
    set1.add(sum(element))
answer = list(prime & set1)
answer.sort()
if answer:
    for element in answer:
        print(element, end=" ")
else:
    print(-1)