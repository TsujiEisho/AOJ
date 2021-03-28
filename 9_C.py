n = int(input())
T, H = 0, 0
for i in range(n):
    taro, hanako = map(str, input().split())
    if taro > hanako:
        T += 3
    elif taro < hanako:
        H += 3
    else:
        T+=1; H+=1
print(T, H)