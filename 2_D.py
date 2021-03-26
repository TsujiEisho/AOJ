w, h, x, y, r = map(int, input().split())

"""
円は中心からの距離が等しい。
半径rだからこれがw,hを超えなければよい
"""

if (r <= x <= w-r) and (r <= y <= h-r):
    print("Yes")
else:
    print("No")