n, m = map(int, input().split())

A = [[] for i in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))

B = []
for i in range(m):
    B.append(int(input()))

for i in range(n):
    ans = 0
    for j in range(m):
        a, b = A[i][j], B[j]
        ans += a*b
    print(ans)
