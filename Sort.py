a = 8
b =18
c = 48

if a >= b >= c:
    print(c, b, a)
else:
    if a >= c >= b:
        print(b, c, a)
    else:
        if b >= a >= c:
            print(c, a, b)
        else:
            if b >= c >= a:
                print(a, c, b)
            else:
                if c >= a >= b:
                    print(b, a, c)
                else:
                    if c >= b >= a:
                        print(a, b, c)
