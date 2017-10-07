for _ in range(int(input())):
    s = input()
    flag = False
    if s==s[::-1]: # Whole string is Palindrome
        flag = True
    else :
        n = len(s)
        for i in range(2, min(3,n)): #length of substring (max length 3)
            for j in range(n-i):
                temp = s[j:j+i]
                if temp == temp[::-1]:
                    flag = True
                    break
    if flag:
        print("YES")
    else:
        print("NO")
		
'''
If a SubString is Palindrome, then its smallest part must be of length 2 (for SubString of even length) or 3 (for SubString of odd length) that will also be Palindrome. Here we consider that the length of the palindrome string is greater than 1. So, for this problem, we just find if there is any substring of length 2 or 3 that exists which is palindrome, then we can conclude that there must be a substring of 's' which will be Palindrome. We donot need to find Palindrome SubString of length greater than three. Because that is already considered while we find Palindrome SubString of length 2 or 3.
'''
