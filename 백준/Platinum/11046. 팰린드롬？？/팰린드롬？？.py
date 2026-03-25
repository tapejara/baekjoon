import sys
input = sys.stdin.readline
def maancher(arr0):
    arr1 = [0 for _ in range(len(arr0))]
    l = -1
    r = -1
    for i in range(len(arr0)):
        if(i > r):
            k = 1
        else:
            k = min(arr1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and arr0[i - k] == arr0[i + k]:
            k += 1
        arr1[i] = k
        k -= 1
        if(i + k > r):
            l = i - k
            r = i + k
    arr2 = [0 for _ in range(len(arr0))]
    l = -1
    r = -1
    for i in range(len(arr0)):
        if(i > r):
            k = 0
        else:
            k = min(arr2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < n and arr0[i - k - 1] == arr0[i + k]:
            k += 1
        arr2[i] = k
        k -= 1
        if(i + k > r):
            l = i - k - 1
            r = i + k
    return arr1, arr2
n = int(input())
list0 = list(map(int,input().split()))
list1, list2 = maancher(list0)
t = int(input())
for _ in range(t):
    s, e = map(int,input().split())
    s -= 1
    e -= 1
    if((e - s) % 2 == 1):
        if((e - s) // 2 + 1 <= list2[(s + e) // 2 + 1]):
            print(1)
        else:
            print(0)        
    else:
        if((e - s) // 2 + 1 <= list1[(s + e) // 2]):
            print(1)
        else:
            print(0)