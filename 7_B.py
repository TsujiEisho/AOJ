import itertools

while True:

    n, x = map(int, input().split())
    if n==x==0:
        exit()
    else:
        ans = 0
        U = list(range(1, n+1))
        index = itertools.combinations(U, 3)
        for i in index:
            a, b, c = i
            if a+b+c == x:
                ans += 1

        print(ans)