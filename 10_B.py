a, b, C = map(int, input().split())
import math
# cはもう一つの辺
S = a*b*math.sin(math.radians(C))/2

c = math.sqrt(a**2 + b**2 -2*a*b*math.cos(math.radians(C)))
L = a+b+c

h = 2*S/a

print(S)
print(L)
print(h)
