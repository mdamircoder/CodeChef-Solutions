for i in range(int(input())):
    size, p = map( int, input().split())
    ans = ""
    if p>2:
        arr = ['a'] * p
        inp = ['a', 'b']
        for i in range(1,p//2):
            arr[i] = inp[i%2]
            arr[p-i-1] = arr[i]
        if p%2==1:
            arr [p//2] = inp[(p//2)%2]
        ans = "".join(arr)
        ans = ans * (size//p)
        print(ans)
    else: #p = 1, 2
        print("impossible")
# 100 %
