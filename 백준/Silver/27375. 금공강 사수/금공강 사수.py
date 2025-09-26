import sys
input = sys.stdin.readline
n, k = map(int,input().split())
list1 = [list(map(int,input().split())) for _ in range(n)]
answer = 0
time = [[0 for _ in range(11)] for _ in range(6)]
def function(score, arr1, arr2):
    global answer
    if(score == k):
        answer += 1
    else:
        for i in range(len(arr2)):
            if(arr2[i][0] == 5):
                continue
            else:
                flag = True
                for j in range(arr2[i][1], arr2[i][2] + 1):
                    if(arr1[arr2[i][0]][j] == 1):
                        flag = False
                if(flag == True):
                    arr3 = []
                    for j in range(len(arr1)):
                        temp = arr1[j].copy()
                        arr3.append(temp)
                    for j in range(arr2[i][1], arr2[i][2] + 1):
                        arr3[arr2[i][0]][j] = 1
                    function(score + (arr2[i][2] - arr2[i][1] + 1), arr3, arr2[i + 1:])
function(0,time,list1)
print(answer)