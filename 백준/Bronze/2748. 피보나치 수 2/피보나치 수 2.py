n = int(input())
f = [0, 1]
for i in range(2, 91):
    f.append(f[i - 2] + f[i - 1])
print(f[n])