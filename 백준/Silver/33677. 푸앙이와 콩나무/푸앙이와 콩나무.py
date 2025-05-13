n = int(input())
tree = [(1000000, 1000000) for _ in range(n + 1)]
tree[0] = (0, 0)
for i in range(n + 1):
    if(i + 1 < n + 1):
        tree[i + 1] = min(tree[i + 1], (tree[i][0] + 1, tree[i][1] + 1))
    if(i * 3 < n + 1):
        tree[i * 3] = min(tree[i * 3], (tree[i][0] + 1, tree[i][1] + 3))    
    if(i ** 2 < n + 1):
        tree[i ** 2] = min(tree[i ** 2], (tree[i][0] + 1, tree[i][1] + 5))
print(tree[n][0], tree[n][1])