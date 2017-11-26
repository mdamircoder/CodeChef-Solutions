for _ in range(int(input())):
    size = int(input())
    List = list(map(int, input().split()))
    minValIndexes = List.index(min(List))
    print(minValIndexes+1)

    
''' The i-th value is considered twice in the sum.

During PrefixSum(i), we calculate a[1]+a[2]+a[3]+...+a[i]
During SuffixSum(i), we calculate a[i]+a[i+1]+a[i+2]+...+a[n]

Consider 1-indexed list

So the sum would be minimum for minimum value of a[i]
that is, a[i] should be the minimum value of that list

There could be one or more minimum values. We need to find the minimum
value of i such that a[i] = min (a[i])

a.index(min(a)) method does that work. It returns the minimum
value of i such that a[i] = min (a[i]) where i is 0-indexed value
for this function. So we need to add 1 ti find the corresponding value
for 1-indexed list.  '''
