def maancher(s):
    arr1 = [0 for _ in range(len(s))]
    l = -1
    r = -1
    for i in range(len(s)):
        if(i > r):
            k = 1
        else:
            k = min(arr1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
            k += 1
        arr1[i] = k
        k -= 1
        if(i + k > r):
            l = i - k
            r = i + k
    arr2 = [0 for _ in range(len(s))]
    l = -1
    r = -1
    for i in range(len(s)):
        if(i > r):
            k = 0
        else:
            k = min(arr2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < len(s) and s[i - k - 1] == s[i + k]:
            k += 1
        arr2[i] = k
        k -= 1
        if(i + k > r):
            l = i - k - 1
            r = i + k
    return arr1, arr2
s = input()
list1, list2 = maancher(s)
a = max(2 * x - 1 for x in list1)
b = max(2 * x for x in list2)
print(max(a, b))