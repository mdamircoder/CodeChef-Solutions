t = int(input())
for i in range(t):
    n = int(input())
    remaining = n - 92680
    temp=37076
    for i in range(1, 92681):
        print(i, end=" ")
    for i in range(remaining):
        if i==(remaining-1):
            print(37077-i)
            break
        else:
            print("1 ", end="")
'''
1, 2, 3, 92680
Then
1, 1, 1, .... 1, (37077-i)
----------------------------
In this prefSum[i]=suffSum[i] , elem[i] is considered twice.
So, for the maximum element, the sum should be >= 2^32
-------------------------
Now,
(1+2+3+....92680)+92680 = 92681*92680//2+92680
=4294930220

2^32 - 4294930220 = 37076
Now if there are n elements, we will have to distribute the elements in such a way,
Sum of last (n-92680) elements >=37076, but not too greater.
-----------------
I made those rest of the elements as 1, 1, 1... , 1, (37077-(n-92680-1))
This will sum upto 37077

'''
