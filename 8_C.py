l = [0 for i in range(26)]

while True:
    try:
        s = list(input().lower())
        for i in s:
            try:
                l[ord(i) - ord("a")] += 1
            except:
                pass

    except EOFError:
        break


# 出力
c = 0
for i in l:
    print(chr(97+c), ":", i)
    c+=1