n = int(input())
min, max= 0, n
while min<=max:
    mid = (min + max) // 2
    if(mid ** 2 >= n):
        max = mid - 1
    else:
        min = mid + 1
print(min)