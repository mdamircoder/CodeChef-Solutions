for _ in range(int(input())):
    s = input().strip()
    names = s.split(" ")
    for i in range(len(names)):
        if i==len(names)-1:
            st = names[i].upper()
            print(st[0], end="")
            print( st[1:].lower(), end="" )
        else:
            st = names[i].upper()
            print( st[0], end=". ")
    print()
		'''
	Simple Problem
	
	gandhi -> Gandhi
	mahatma gandhI -> M. Gandhi
	Mohndas KaramChand gandhi -> M. K. Gandhi
	_________________________________________
	We first input the name as String, then split by spaces(" ") and store in a list 'names'
	
	If len(names) > 1, then the name has more than one parts. Otherwise only one part.
	Whatever it is, if the index represents the last element of that list 'names' (i.e. i == len(names), for 1-indexed concept),
					then first convert all letters of names[i] string into Capital letter and print the first character
					then convert all characters into Small letters, then print the rest portion, i.e. (names[i]).lower()[1:]
	For other list elements, just convert all characters into Capital, Print first character, then a dot(".") and a space(" ")
	
	string_name.lower() converts all characters into Small letters of that string_name.
	string_name.upper() converts all characters into Capital letters of that string_name.
	
	If st is a string, then st[begin:(end+1)] represents the substring of st from 'begin' index to end 'index', by default 'begin'=0 and 'end'=len(st)-1 .
	'''
