n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
import math

def P_1(n, X, Y):
    ans = 0
    for i in range(n):
        ans += abs(X[i] - Y[i])
    return ans

def P_2(n, X, Y):
    ans = 0
    for i in range(n):
        ans += abs(X[i] - Y[i])**2
    return math.sqrt(ans)

def P_3(n, X, Y):
    ans = 0
    for i in range(n):
        ans += abs(X[i] - Y[i])**3
    return ans**(1/3)


def P_inf(n, X, Y):
    ans = 0
    for i in range(n):
        g = abs(X[i] - Y[i])
        ans = max(ans, g)
    return ans

print(P_1(n, X, Y))
print(P_2(n, X, Y))
print(P_3(n, X, Y))
print(P_inf(n, X, Y))
