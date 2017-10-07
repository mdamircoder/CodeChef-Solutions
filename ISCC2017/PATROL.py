for _ in range(int(input())):
    u, v, x = map(int, input().strip().split(" "))
    t = x/(u+v)
    print(t)
	
'''
Very simple problem. One person is moving with velocity u metre/second, another with velocity v metre/second opposite direction to each other.

The maximum distance for which walkie-talkie will remain operative is x metre. How long (time) they can communicate maximum ?

Let the time be t seconds (maximum time upto which walkie-talkie will remain operative).
First person covers (u.t) metre distance in t seconds.
Second person covers (v.t) metre distance in t seconds.

So, u.t + v.t = x (t is max, so the distance must be max, i.e. x metre)
So, t = x/(u+v) seconds.
'''
