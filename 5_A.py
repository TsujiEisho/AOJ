while True:
    h, w = map(int, input().split())
    if h==0 and w==0:
        exit()
    for i in range(h):
        print("#"*w)

    print("")

