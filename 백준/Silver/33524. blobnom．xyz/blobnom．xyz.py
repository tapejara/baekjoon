n, m = map(int,input().split())
list1 = [3* (i ** 2) - 3 * i + 1 for i in range(n + 1)]
list1[0] = 0
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
def function1(num):
    minimum, maximum = 0, len(a) - 1
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if(num < a[mid]):
            maximum = mid - 1
        else:
            minimum = mid + 1
    return maximum
def function2(num):
    minimum, maximum = 0, len(list1) - 1
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if(num < list1[mid]):
            maximum = mid - 1
        else:
            minimum = mid + 1
    return maximum
for i in b:
    p = function1(i) + 1
    print(function2(p))