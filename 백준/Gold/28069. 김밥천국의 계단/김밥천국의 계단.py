n, k = map(int,input().split())
if(k >= n):
    print("minigimbob")
else:
    s = [i for i in range(n + 1)]
    for i in range(3, n + 1):
        if(i + 1 <= n and s[i] + 1 <= k):
            s[i + 1] = min(s[i] + 1, s[i + 1])
        if(i + (i // 2) <= n and s[i] + 1 <= k):
            s[i + (i // 2)] = min(s[i] + 1, s[i + (i // 2)])
    if(s[n] <= k):
        print("minigimbob")
    else:
        print("water")