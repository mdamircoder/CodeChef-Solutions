
for i in range(int(input())):
    
    n, target = map(int ,input().split())
    a = list(map(int ,input().split())) #  Distinct elements
    flag = "YES"
    check = {}
    check[ a[0] ] = 1
    prevMax = 1000000001
    prevMin = 0
    
    if n>2:
        
        for i in range(n-1):
            
            if a[i] > target:
                if a[i] < prevMax : # prevMax > a[i] > target
                    prevMax = a[i]
                else:
                    flag = "NO"
                    break

            else: # a[i] < target
                if a[i] > prevMin : # target > a[i] > prevMin
                    prevMin = a[i]
                else:
                    flag = "NO"
                    break
        
    print(flag)

#100 
