n = int(input())
t = list(map(int,input().split()))
a = [0] + t
d = [0]
x = [0]
for i in range(1, n + 1):
    if(a[i] > x[-1]):
        x.append(a[i])
        d.append(len(d))
    elif(a[i] < x[-1]):
        minimum, maximum = 0, len(x) - 1
        while minimum <= maximum:
            mid = (maximum + minimum) // 2
            if(a[i] <= x[mid]):
                maximum = mid - 1
            else:
                minimum = mid + 1
        x[minimum] = a[i]
print(d[-1])