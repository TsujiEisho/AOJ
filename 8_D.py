"""
文字列sを二個並べたものの中にpがあるかどうかで判定できる。
"""


s = str(input())
p = str(input())

s = s*2
for i in range(len(s)-len(p)):
    if s[i:i+len(p)] == p:
        print("Yes")
        exit()
print("No")