n = int(input())
ans = []


for i in range(1, n+1):
    x = i

    if x%3 == 0:
        ans.append(str(i))
        continue

    if x > 10:
        u = list(str(x))
        if "3" in u:
                ans.append(str(x))


print(" "+" ".join(ans))
# print(" 3 6 9 12 13 15 18 21 23 24 27 30 31 32 33 34 35 36 37 38 39 42 43 45 48 51 53 54 57 60")