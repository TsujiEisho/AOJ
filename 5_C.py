while True:
    h, w = map(int, input().split())
    if h==w==0:
        exit()

    else:
        if h%2 == 0:
            if w%2 == 0:
                for i in range(h//2):
                    print("#."*(w//2))
                    print(".#"*(w//2))
            elif w%2 == 1:
                for i in range(h//2):
                    print("#"+".#"*(w//2))
                    print("."+"#."*(w//2))


        elif h%2 == 1:
            if w%2 == 0:
                for i in range(h//2):
                    print("#."*(w//2))
                    print(".#"*(w//2))
                print("#."*(w//2))
            elif w%2 == 1:
                for i in range(h//2):
                    print("#"+".#"*(w//2))
                    print("."+"#."*(w//2))
                print("#" + ".#" * (w // 2))

    print()





