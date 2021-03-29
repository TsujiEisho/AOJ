import math
while True:
    n = int(input())
    if n == 0:
        exit()
    else:
        s = list(map(int, input().split()))
        m = sum(s)/len(s)
        std = 0
        for i in s:
            std += (i - m)**2
        print(math.sqrt(std/len(s)))
