t = int(input())
for ii in range(t):
    n, k = map( int, input().split() )
    a = list ( map( int, input().split() ) )
    a = list(set(a)) #Duplicate elements exist here
    a.sort()
    n = len(a)
    j = 0
    MEX = 0
    if k<a[0]:
        MEX=k
    else:
        for i in range(a[n-1]+k+1):
            if j>=n :
                MEX += k
                break
            if i==a[j]:
                MEX += 1
                j += 1
            else:
                if k==0:break
                else: # i is inserted in a (imagine)
                    k-=1
                    MEX += 1
    print(MEX)

'''
First we need to check whether there are any duplicate elements.
If present, no need to consider them to find MEX value.
So remove them.
---------------------------------------------------------------
To know what is MEX value, please visit
https://en.wikipedia.org/wiki/Mex_(mathematics)
---------------------------------------------------------------
We can add maximum k integer values in that set, if necessary.
So we start checking it from 0, as it's the minimum possible integer.
We need to check the minimum non-negative integer value missing from that set.
---------------------------------------------------------------
We check whether any number (from 0, simultaneously) is absent in that set.
If it is possible to add (k>=1) we add that missing value in that set, then
decrease the value of k by 1.
Else we stop. (Any number is missing and k<1).
That missing integer will be our required MEX value.
---------------------------------------------------------------
Here instead of adding that missing value in that set, I have just
decreased the value of k by 1, i.e. quivalent to adding that value.
---------------------------------------------------------------
I have also sorted that set, so that the searching can be done efficiently.
---------------------------------------------------------------
I used a loop, starting from 0, its ending must be > max element of set.
The loop variable checks the integer values to which we need to compare.
---------------------------------------------------------------
I also used an index j, which indicates which element of the sorted set is
to be compared. If insertion is possible, then instead fo inserting, didn't
update the value of j (index variable for elements of set)
'''
