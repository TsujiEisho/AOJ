import math

x1, y1, x2, y2 = map(float, input().split())

length = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
print(length)