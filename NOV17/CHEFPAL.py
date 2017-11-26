
vocab = 'abcdefghijklmnopqrstuvwxyz'
import math
for i in range(int(input())):
    
    size, var = map( int, input().split() )
    ans = ""
    
    if var == 1 : # A = 1
        ans = 'a' * size
        print(size, ans)
        
    elif var == 2: # A = 2
        
        if size==1:
            ans = '1 a'
            print(ans)
            
        elif size==2:
            ans = '1 ab'
            print(ans)
        elif size==3: print("2 aab") # aa b
        
        elif size==4: print("2 aabb") # aa bb
        
        elif size==5: print("3 aaabb") # aa ba b (3)
        
        elif size==6: print("3 aaabbb") # aa ba bb (3)
        
        elif size<=10: # aaaa ba bbb   or    aaaa ba bbbb
            ans = 'ba'
            size -= 2
            b = size // 2
            a = size - b
            ans = str(a) + " " + 'a'*a + ans + 'b'*b
            print(ans)
    
        else : #size > 10
            source = 'babaabbabaab' #(baba)(abba)(baab)....
            ans = source * (size//12)
            rem = size % 12
            ans = '4 ' + ans + source[:rem]
            print(ans)

    else: # A >= 3
        ans = '1 '
        cnt = size // var
        rem = size % var
        ans = ans + vocab[:var]*cnt
        ans += vocab[:rem]
        print(ans)
# 100
