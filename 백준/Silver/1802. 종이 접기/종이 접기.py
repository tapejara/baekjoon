import sys
input = sys.stdin.readline
t = int(input())
def function(arr):
    if(len(arr) == 1):
        return arr
    elif(len(arr) == 3):
        if(arr[0] != arr[2]):
            return arr
        else:
            return [-1] * 3
    else:
        if(-1 in arr):
            return [-1] * len(arr)
        else:
            flag = True
            for i in range(len(arr) // 2):
                if( arr[i] == arr[len(arr) - (1 + i)]):
                    flag = False
            if(flag == True):
                return function(arr[:len(arr) // 2]) + [arr[len(arr) // 2]] + function(arr[len(arr) // 2 + 1:])
            else:
                return [-1] * len(arr)
for _ in range(t):
    temp = input().strip()
    list1 = [i for i in temp]
    if(function(list1) == list1):
        print("YES")
    else:
        print("NO")