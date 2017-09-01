for _ in range(int(input())):
    n = int(input())
    s=input().strip() # Input String which is actually an array of integer values
    a=[]
    flag=True #Flag = True indicates the array satisfies the condition
    for w in s.split(" "): 
        if int(w) not in a:
            a.append(int(w))
    #print(a)
    if(len(a)!=7) or min(a)!=1 or max(a)!=7:
        flag=False
    elif s!=s[::-1]:
        flag=False
    else:
        for i in range (len(a)-1):
            if int(a[i])>int(a[i+1]):
                flag=False
                break
    if(flag): print("yes")
    else: print("no")
	
'''
s is the input array, stored as string. We need to check whether s is a Rainbow array (satisfies the condition)

a is the list of elements present in array, stored serially as occured in that array. Only the first occurance is considered.

	Condition 2 : the array (input taken as string) must be of palindromic. If it isn't then flag is False.

	Condition 1 : the occurance of number starts from 1, either reamins same or increases by one upto 7 and then similarly, decreases upto 1.
If the len(a) is not 7, then 1 to 7 - all elements aren't there, or may be some more different (like 8, 9, 10...) numbers are present there.
It may also happen that it starts from 2 and ends to 8, then len(a) = 7. So we need to check min(a)==1 ? and max(a)==7 ? So if all elements between 1 to 7 aren't (upto reaching 7), the flag becomes False.

	Condition 3 : Condition 1 and 2 are true, Now we need to check whether the numbers in array starts from 1, either reamins same or increases by one upto 7 and then similarly, decreases upto 1.
We just need to check the occurances in list 'a' from 1 to occurance of 7, if this is maintained, then the rest portion will also maintain, as the array is palindrome upto this level.
So we check whether the elements has occured serially in 'a' or not. if they occur serially in 'a', it means the numbers in array starts from 1, either reamins same or increases by one upto 7 and then similarly, remains same or decreases upto 1.
If this is not maintained, the flag = False.

We just need to check the conditions for which they are not RAINBOW type. otherwise, it is a RAINBOW array. So flag initialised as True.

'''
