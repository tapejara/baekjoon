for i in range(2,101):
    for j in range(2,101):
        for k in range(2,101):
            for l in range(2,101):
                if(i ** 3 == j **3 + k ** 3 + l ** 3 and j <= k <= l):
                    print(f"Cube = {i}, Triple = ({j},{k},{l})")