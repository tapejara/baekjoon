n, m = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
list1 += [0]
list2 = []
def function(count, arr1, arr2):
    if(count == m + 1):
        for i in range(len(arr2) - 1):
            print(arr2[i], end = " ")
        print(arr2[-1])
    else:
        for i in range(len(arr1) - 1):
            if(arr1[i] != arr1[i - 1]):
                list3 = arr2.copy()
                list3.append(arr1[i])
                function(count + 1, arr1, list3)
function(1, list1, list2)