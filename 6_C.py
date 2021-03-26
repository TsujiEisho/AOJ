n = int(input())

L = [[["0" for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    b, f, r, v = map(int, input().split())
    L[b-1][f-1][r-1] = str(int(L[b-1][f-1][r-1]) + v)
    if int(L[b-1][f-1][r-1]) < 0:
        L[b - 1][f - 1][r - 1] = "0"

for tou in range(4):
    for kai in range(3):
        print(" "+ " ".join(L[tou][kai]))
    if tou < 3:
        print("####################")