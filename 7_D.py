n, m, l = map(int, input().split())
A = [[] for i in range(n)]
B = [[] for i in range(m)]
C = [[0 for i in range(l)] for i in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(m):
    B[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]

for i in range(n):
    print(" ".join(map(str, C[i])))