while True:
    n = float(input())
    if(n < 0):
        exit()
    print(f"Objects weighing {"%0.2f" % (n)} on Earth will weigh {"%0.2f" % (n * 0.167)} on the moon.")