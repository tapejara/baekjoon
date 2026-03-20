import sys
input = sys.stdin.readline
def ccw(a,b,x,y,n,m):
    return (a*y + x*m + n*b)-(a*m + x*b + n*y)
n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
list1.sort(key=lambda x:x[4])
list2 = [set() for _ in range(n)]
answer = 0
for i in range(n):
	for j in range(i + 1, n):
		point1 = ccw(list1[i][0], list1[i][1], list1[i][2], list1[i][3], list1[j][0], list1[j][1]) * ccw(list1[i][0], list1[i][1], list1[i][2], list1[i][3], list1[j][2], list1[j][3])
		point2 = ccw(list1[j][0], list1[j][1], list1[j][2], list1[j][3], list1[i][0], list1[i][1]) * ccw(list1[j][0], list1[j][1], list1[j][2], list1[j][3], list1[i][2], list1[i][3])
		if(point1 < 0 and point2 < 0):
			list2[i].add(j)
for i in range(n):
	answer += list1[i][4] * (len(list2[i]) + 1)
print(answer)