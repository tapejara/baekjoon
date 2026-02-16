n = int(input())
list1 = ["STRAWBERRY", "BANANA", "LIME", "PLUM"]
list2 = [0, 0, 0, 0]
for _ in range(n):
    a, b = input().split()
    list2[list1.index(a)] += int(b)
if(5 in list2):
    print("YES")
else:
    print("NO")