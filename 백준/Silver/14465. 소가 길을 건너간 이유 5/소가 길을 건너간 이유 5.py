import sys
input = sys.stdin.readline
n, k, b = map(int,input().split())
signal = [0 for _ in range(n)]
for _ in range(b):
    signal[int(input()) - 1] = 1
for i in range(k):
    if(signal[i] == 1):
        signal[i] = -1
answer = signal.count(-1)
flag = answer
for i in range(1, n - k + 1):
    if(flag > 0 and signal[i - 1] != 0):
        flag -= 1
    if(signal[i + k - 1] == 1):
        flag += 1
    answer = min(flag, answer)
print(answer) 