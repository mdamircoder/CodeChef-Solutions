for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    flag = "*"
    if s==t : # B wins -> 'ww' form
        flag="B"
    else :
        for i in range(len(s)-1):
            if ( s[i] in s[i+1:] ) and ( s[i] not in t[:] ): # Repeatation of any letter in s, not present in t
                flag="A"    # A wins -> 'wuw' form
                break
    if flag=="*": print("B") # A cannot win, so B wins.
    else: print(flag)
    
'''
===========================================================
Remeber , the palindromic string must be of length > 1 .
Shortest palindromic string of even length 'ww'
Shortest palindromic string of odd length 'wuw'
Any palindromic string of even length must have 'ww'-form substring in its middle position.
And any palindromic string of odd length must have 'wuw'-form substring in its middle position.
===========================================================
We donot need to check whether B wins or not. Except 2nd move of the game.
We need to check - whether A wins or not ?
-----------------------------------------------------------
Because even if none can make a palindromic string, B wins .
-----------------------------------------------------------
2nd move of the game - first move of B . If B can enter the same character entered by A, B wins.
B wins by making 'ww'-formed palindrome string.
-----------------------------------------------------------
A and B both play optimally.
B first tries to make 'ww'-formed string in his first move (2nd move of the game).
If B fails in 2nd move of the game (B's first), A tries for 'wuw'-formed string.
===========================================================
B can make 'ww'-formed string only if s==t .
[ Where, s is the input string of A, and t is the input string of B . ]
Because, even if a single char of s doesn't match with t, A will enter that char first. So that B can't form 'ww'.
-----------------------------------------------------------
Then we check whether there is any repeation of char in s (i/p str. of A).
If there is any repeation of a char in s which is not present in t, A wins in his 2nd move (3rd move of the game) by 'wuw'-formed palindrome string.
===========================================================
'''
