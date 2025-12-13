while True:
    try: 
        n, k = map(int,input().split())
        answer = n
        while n >= k:
            temp = n % k
            n //= k
            answer += n
            n += temp
        print(answer)
    except:
        exit()