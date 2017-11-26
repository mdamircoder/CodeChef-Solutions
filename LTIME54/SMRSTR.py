def func(prod, x):
    x = x // prod
    print( x , end=" ")

for ii in range(int(input())):
    n, q = map( int, input().split() )
    arr = list(map( int, input().split() ))

    prod = arr[0]
    for i in range(1, n):
        prod *= arr[i]
    
    quer = list(map( int, input().split() ))
    for j in range(q):
        x = quer[j]
        func( prod, x)
    print()
    
#100
