r, c = map(int, input().split())
ans = [[] for _ in range(r+1)]

# 入力と行の和
for i in range(r):
    ans[i] = list(map(int, input().split()))
    ans[i].append(sum(ans[i]))


# 列の和
for i in range(c+1):
    s = 0
    for j in range(r):

        s += ans[j][i]
    ans[r].append(s)


# 出力
for i in range(r+1):
    print(" ".join(map(str, ans[i])))