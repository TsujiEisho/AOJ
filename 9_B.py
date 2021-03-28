while True:
    S = str(input())
    if S == "-":
        exit()
    m = int(input())
    for i in range(m):
        h = int(input())
        S += S[:h]
        S = S[h:]
    print(S)
