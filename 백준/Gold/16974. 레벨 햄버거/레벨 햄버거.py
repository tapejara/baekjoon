n, x = map(int,input().split())
hamburger = [(1,1)]
for i in range(n):
    a, b = hamburger[-1]
    hamburger.append((a * 2 + 3, b * 2 + 1))
def function(layer, count, level):
    if(layer == 0):
        return count
    else:
        for i in range(level, -1, -1):
            if(hamburger[i][0] > layer):
                layer -= 1
                level -= 1
                if(layer == 0):
                    return function(layer, count, level)
            elif(hamburger[i][0] <= layer):
                layer -= hamburger[i][0]
                count += hamburger[i][1]
                if(layer >= 1):
                    layer -= 1
                    count += 1
                return function(layer, count, level)
print(function(x, 0, n))