t = int(input())
while ( t > 0) :
    t = t -1 
    n = int(input())
    if (n < 10 ) : 
        print(n)
    else :
        s = list(str(n))
        for i in range(len(s)-1,0,-1) :
            if (int(s[i]) >= 5) :
                # print(s[i-1])
                s[i-1] = str(int(s[i-1]) + 1)
                # print(s[i-1])
            s[i] = str(0)
        print("".join(s))