import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [i for i in range(1, n + 1)]
list2 = []
def function(count, arr1, arr2):
    if(count == m + 1):
        for i in range(len(arr2)):
            if(i == len(arr2) - 1):
                print(arr2[i])
            else:
                print(arr2[i], end= " ")
    else:
        for element in arr1:
            if(element not in arr2):
                list3 = arr2.copy()
                list3.append(element)
                function(count + 1, arr1, list3)
function(1, list1, list2)