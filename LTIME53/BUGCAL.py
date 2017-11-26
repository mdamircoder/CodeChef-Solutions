for ii in range(int(input())):
    a, b = map( int, input().split())
    aa = a%10
    bb = b%10
    res = str( (aa+bb)%10 )
    a = a//10
    b = b//10
    while True:
        if a==0 or b==0:
            if a==0 and b!=0:
                res = str(b) + res
            elif b==0 and a!=0:
                res = str(a) + res
            break
        else:
            aa = a%10
            bb = b%10
            res = str( (aa+bb)%10 ) + res
            a = a//10
            b = b//10
    print(int(res))
#100
