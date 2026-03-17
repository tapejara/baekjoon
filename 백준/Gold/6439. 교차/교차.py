import sys
input = sys.stdin.readline
def ccw(a,b,x,y,n,m):
    return (a*y + x*m + n*b) - (a*m + x*b + n*y)
t = int(input())
for _ in range(t):
    l1 = list(map(int,input().split()))
    line = [l1[i] for i in range(4)]
    sq = [[l1[4], l1[5], l1[4], l1[7]], [l1[4], l1[5], l1[6], l1[5]], [l1[6], l1[7], l1[6], l1[5]], [l1[6], l1[7], l1[4], l1[7]]]
    answer = "F"
    if((min(l1[4],l1[6]) <= line[0] <= max(l1[4],l1[6]) and min(l1[5],l1[7]) <= line[1] <= max(l1[5],l1[7])) or(min(l1[4],l1[6]) <= line[2] <= max(l1[4],l1[6]) and min(l1[5],l1[7]) <= line[3] <= max(l1[5],l1[7]))):
        answer = "T"
    for l in sq:
        a = ccw(l[0], l[1], l[2], l[3], line[0], line[1])
        b = ccw(l[0], l[1], l[2], l[3], line[2], line[3])
        c = ccw(line[0], line[1], line[2], line[3], l[0], l[1])
        d = ccw(line[0], line[1], line[2], line[3], l[2], l[3])
        point1 = a * b
        point2 = c * d
        if(point1 < 0 and point2 < 0):
            answer = "T"
        elif(point1 == 0 and point2 == 0):
            if(a == 0 and min(l[0],l[2]) <= line[0] <= max(l[0],l[2]) and min(l[1],l[3]) <= line[1] <= max(l[1],l[3])):
                answer = "T"
            elif(b == 0 and min(l[0],l[2]) <= line[2] <= max(l[0],l[2]) and min(l[1],l[3]) <= line[3] <= max(l[1],l[3])):
                answer = "T"
            elif(c == 0 and min(line[0],line[2]) <= l[0] <= max(line[0],line[2]) and min(line[1],line[3]) <= l[1] <= max(line[1],line[3])):
                answer = "T"
            elif(d == 0 and min(line[0],line[2]) <= l[2] <= max(line[0],line[2]) and min(line[1],line[3]) <= l[3] <= max(line[1],line[3])):
                answer = "T"
    print(answer)