for _ in range(int(input())):
    n = input()
    for i in range(6,10): # 6 to 9
        if str(i) in n: # So you need to print something
            if i==6: #6
                for j in range(5, 10): # 5 to 9
                    if i==j and ( n.count("6") )>1:
                        num = i*10 + j
                        ch = chr(num)
                        print(ch, end="")
                    elif i!=j and str(j) in n:
                        num = i*10 + j
                        ch = chr(num)
                        print(ch, end="")
            elif i==9: #9
                if "0" in n :
                    print("Z", end="")
            else: # 7 , 8
                for j in range(10): # 0 to 9
                    if i==j and ( n.count(str(j)) )>1:
                        num = i*10 + j
                        ch = chr(num)
                        print(ch, end="")
                        
                    elif i!=j and  str(j) in n:
                        num = i*10 + j
                        ch = chr(num)
                        print(ch, end="")
    print()
