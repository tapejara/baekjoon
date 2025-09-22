import itertools
n, k = map(int,input().split())
list1 = [list(map(int,input().split())) for _ in range(n)]
temp = [i for i in range(n)]
list2 = list(itertools.combinations(temp, k))
answer = -1e9
def function(result, count, arr1, arr2):
    for i in range(len(arr1)):
        if(arr1[i] != count and ((count, arr1[i]) not in arr2)):
            arr3 = arr1[i:]
            arr2.append((count, arr1[i]))
            result += function(list1[count][arr1[i]], arr1[i], arr3, arr2)
    return result
for element in list2:
    list3 = []
    b = function(0, element[0], element, list3)
    answer = max(answer, b)
print(answer)