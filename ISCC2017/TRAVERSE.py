for _ in range(int(input())):
    m = int(input())
    if m%3==2:
        x,y = 1,1
        x += (m//3)
        y += (m//3)*2
        print(x,y)
    elif m%3==1:
        x,y = 1,0
        x += (m//3)
        y += (m//3)*2
        print(x,y)
    else: #m%3==0
        x,y = 0,0
        x += (m//3)
        y += (m//3)*2
        print(x,y)

'''
Suhana starts from (0, 0) position.
She takes 1 step towards x axis , and then maximum two steps towards y axis, and so on..
Think about first 3 steps. then find the similarity.

If she takes 3 steps => she has taken two steps towards y axis, and then 1 step towards x axis.
If she takes 2 steps => she has taken two steps towards y axis.
If she takes 1 step => she has taken one step towards y axis.

Let m be the number of steps. X be the steps taken towards x-axis, Y be the steps taken towards y-axis.
Then m//3(integer division) steps has been taken as 1 step towards x axis , and then maximum two steps towards y axis, and so on..
The extra steps are (m - m//3 ), i.e. (m%3)

(m%3)=0 => she has taken no extra steps. 		So, initialised as X=0, Y=0 for this case
(m%3) = 1 => she has taken extra one step towards x axis. 		So, initialised as X=1, Y=0 for this case
(m%3) = 2 => she has taken extra one step towards x axis, and one step towards y axis.		So, initialised as X=1, Y=1 for this case

Finally 
X = X + (m//3),		as Inintially, m//3(integer division) steps has been taken as 1 step towards x axis
Y = Y + (m//3)*2,		as Inintially, (m//3).2 number of steps has been taken towards y axis
'''
