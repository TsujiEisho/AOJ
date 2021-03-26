while True:
    a, op, b = map(str, input().split())
    if op == "?":
        exit()
    else:
        a, b = int(a), int(b)
        if op=="+":
            print(a+b)
        elif op=="-":
            print(a-b)
        elif op=="*":
            print(a*b)
        else:
            print(a//b)


