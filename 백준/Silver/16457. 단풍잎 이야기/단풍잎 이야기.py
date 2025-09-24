import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
q = [list(map(int,input().split())) for _ in range(m)]
answer = []
def function(count, start, arr1):
    if(count == 0):
        temp = 0
        for i in range(len(q)):
            flag = True
            for j in range(k):
                if(q[i][j] not in arr1):
                    flag = False
            if(flag == True):
                temp += 1
            else:
                continue
        answer.append(temp)
    else:
        for i in range(start, 2 * n + 1):
            arr2 = arr1.copy()
            arr2.append(i)
            function(count - 1, i + 1, arr2)
function(n, 1, [])
print(max(answer))