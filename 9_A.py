w = str(input()).lower()
ans = 0

while True:
    l = list(input().split())
    if l[0] == "END_OF_TEXT":
        print(ans)
        exit()
    else:
        for i in l:
            if i.lower() == w:
                ans += 1
