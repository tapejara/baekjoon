n, m = map(int,input().split())
set1 = set(input() for _ in range(n))
set2 = set(input() for _ in range(m))
list1 = list(set1 & set2)
list1.sort()
print(len(list1))
for element in list1:
    print(element)