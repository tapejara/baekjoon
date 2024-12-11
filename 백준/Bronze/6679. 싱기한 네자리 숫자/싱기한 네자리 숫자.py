for i in range(1000,10000):
    a = 0
    b = 0
    c = 0
    d = str(i)
    e = i
    f = i
    for j in range(4):
        a += int(d[j])
    while i >= 12:
        b += i % 12
        i //= 12
        if i < 12:
            b += i
    while e >= 16:
        c += e % 16
        e //= 16
        if e < 16:
            c += e
    if a == b == c:
        print(f)