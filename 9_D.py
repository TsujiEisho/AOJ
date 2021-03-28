S = list(input())
q = int(input())

for i in range(q):
    X = list(map(str, input().split()))

    if X[0] == "print":
        a , b = int(X[1]), int(X[2])+1
        print("".join(S[a: b]))

    elif X[0] == "replace":
        a, b = int(X[1]), int(X[2]) + 1
        u = 0
        for i in range(a, b):
            S[i] = (X[3])[u]
            u += 1

    elif X[0] == "reverse":
        a, b = int(X[1]), int(X[2]) + 1
        Z = S[a:b]
        Z = Z[::-1]
        u = 0
        for i in range(a, b):
            S[i] = Z[u]
            u += 1