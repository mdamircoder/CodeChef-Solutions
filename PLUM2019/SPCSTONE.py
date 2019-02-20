# 100
# Thanos planet solved : SPCSTONE


import math

d = int(input())
d1, n = map(int, input().split())
planet = list( map(int, input().split()) )
planet.append(d1)

cnt = 0

prev_pos = 0

i=0
while i < (n+1):
    
    diff = planet [i] - prev_pos

    tot = math.ceil( diff/d )

    cnt += tot

    skip = 0
	# 1000 1200 1800 : go 1000 to 1800 (when max dist is 1000)
    while( i<(n+1) and ( prev_pos+tot*d ) >= planet[i] ):
        i += 1
        skip = 1
        #print(cnt, prev_pos)

    if skip==0 :
        i += 1
        
    prev_pos = planet [i-1]
    

print(cnt)
