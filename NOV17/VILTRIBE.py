for _ in range(int(input())):
    s = input()
    a = s.count("A")
    b = s.count("B")
    cnt = 0
    prev = ""
    for w in s:
        if prev != "" and prev=="A":
            if w==".":
                cnt += 1
            elif w=="A":
                a += cnt
                cnt = 0
            else: # w = "B"
                cnt = 0
                prev = w
        elif prev != "" and prev=="B":
            if w==".":
                cnt += 1
            elif w=="B":
                b += cnt
                cnt = 0
            else: # w = "A"
                cnt = 0
                prev = "A"
        elif prev=="" and w!=".":
            prev = w
    print(a, b)
#100
