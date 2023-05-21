t = int(input())
for i in range(0,t):
    s1 = list(input())
    s2 = list(input())
    print("Test ",end="")
    print(i+1,end="")
    s1.sort()
    s2.sort()
    l1 = len(s1)
    l2 = len(s2)
    if( l1 != l2):
        print(": NO")
    else:
        res = ": YES"
        for i in range(l1):
            if s1[i] != s2[i]:
                res = ": NO"
                break
        print(res)