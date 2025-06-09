fibonacci = [[1,0], [0,1]]
for i in range(2,41):
    temp = [fibonacci[i - 1][0] + fibonacci[i - 2][0], fibonacci[i - 1][1] + fibonacci[i - 2][1]]
    fibonacci.append(temp)
t = int(input())
for _ in range(t):
    n = int(input())
    print(fibonacci[n][0], fibonacci[n][1])