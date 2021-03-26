"""
採点用の関数を作ってループで回す
"""

def saiten(m, f, r):
    if m==-1 or f==-1:
        ans = "F"
    elif m+f >= 80:
        ans = "A"
    elif m+f >= 65:
        ans = "B"
    elif m+f >= 50:
        ans = "C"
    elif m+f >= 30:
        if r >= 50:
            ans = "C"
        else:
            ans = "D"
    else:
        ans = "F"
    return ans

while True:
    m, f, r = map(int, input().split())
    if m==r==f==-1:
        exit()
    else:
        print(saiten(m, f, r))