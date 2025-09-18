n, m = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
list2 = []
def function(count, arr1, arr2):
    if(count == m + 1):
        for i in range(len(arr2)):
            if(i == len(arr2) - 1):
                print(arr2[i])
            else:
                print(arr2[i], end= " ")
    else:
        for i in range(len(arr1)):
            list3 = arr2.copy()
            list4 = arr1[i:]
            list3.append(arr1[i])
            function(count + 1, list4, list3)
        
function(1, list1, list2)