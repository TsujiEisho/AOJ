n = int(input())
"""
リストを作っておいて，照らし合わせて時にないものを出力
"""

S = list(range(1, 14))
H = list(range(1, 14))
C = list(range(1, 14))
D = list(range(1, 14))

for i in range(n):
    x, y = map(str, input().split())
    y = int(y)
    if x == "S":
        S.remove(y)
    elif x == "H":
        H.remove(y)
    elif x == "C":
        C.remove(y)
    else:
        D.remove(y)

for i in range(len(S)):
    print("S", S[i])
for i in range(len(H)):
    print("H", H[i])
for i in range(len(C)):
    print("C", C[i])
for i in range(len(D)):
    print("D", D[i])


