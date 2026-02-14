t, s = map(int,input().split())
l = [i for i in range(12, 17)]
if(t in l and s == 0):
    print(320)
else:
    print(280)