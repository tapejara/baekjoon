n, k = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort(reverse= True)
while list1:
    a = list1.pop()
    while list1 and a + k >= list1[-1]:
        list1.pop()
        n -= 1
print(n)