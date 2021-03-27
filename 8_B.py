while True:
    x = list(input())
    if x[0] == "0":
        exit()
    else:
        ans = 0
        for i in x:
            ans += int(i)
        print(ans)