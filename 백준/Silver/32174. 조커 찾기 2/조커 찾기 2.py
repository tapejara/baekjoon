import sys
input = sys.stdin.readline
n, m = map(int,input().split())
timeline = [1]
for i in range(m):
    t, c = map(int,input().split())
    if(t == 1): 
        if(timeline[-1] + (c % n) > n):
            timeline.append(timeline[-1] + (c % n) - n)
        else:
            timeline.append(timeline[-1] + (c % n))
    elif(t == 2):
        if(timeline[-1] - (c % n) < 1):
            timeline.append(n + (timeline[-1] - (c % n)))
        else:
            timeline.append(timeline[-1] - (c % n))
    elif(t ==  3):
        timeline.append(timeline[c])
print(timeline[-1])