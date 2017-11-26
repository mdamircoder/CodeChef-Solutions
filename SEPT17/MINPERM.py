for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append((i+1))
        
    for i in range(0,(n-1),2):
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp
 
    if n%2==1:
        temp = a[n-1]
        a[n-1] = a[n-2]
        a[n-2] = temp
    
    for i in range(n):
        if i==(n-1):
            print(a[i])
        else:
            print(a[i], end=" ")
