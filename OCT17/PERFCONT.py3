t = int(input())
for i in range(t):
    prob, participants = map ( int , input().split() )
    solved = list(map ( int , input().split() ))
    hard = 0 # Count of hard category Problem
    cakewalk = 0 # Count of cakewalk category Problem
    flag = True #Chance for being Balanced
    HardMax = participants//10 # Maximum no. of participants who will have to solve the problems, for hard type problem
    CakewalkMin = participants//2 # Min. no. of participants who will have to solve the problems, for Cakewalk type problem
    for w in solved :
        if w <= HardMax : hard += 1 # Satisfies condition of hard problem
        elif w >= CakewalkMin : cakewalk += 1 # Satisfies condition of CakeWalk problem
        if hard >2 or cakewalk>1 : # Violated constrains for being balanced, no need to check
            flag = False
            break
    if flag : # either hard >2 or cakewalk>1
        if hard==2 and cakewalk==1 :# Balanced
            print("yes")
        else:
            print("no")
    else: # Violated constrains earlier, not balanced
        print("no")
