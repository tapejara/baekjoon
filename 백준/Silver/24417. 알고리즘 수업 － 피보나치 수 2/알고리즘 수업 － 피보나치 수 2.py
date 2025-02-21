n = int(input())
fibonacci = [1, 1]
for i in range(1, n - 1):
    fibonacci.append((fibonacci.pop(0) % 1000000007 + fibonacci[0] % 1000000007) % 1000000007)
print(fibonacci[1], (n - 2) % 1000000007)