t = int(input())
while t > 0:
    n = str(input())
    dem = 0 
    for i in range(len(n)-1):
            if n[i] > n[i+1]:
                dem=1
    if dem == 0:
        print("YES")
    else:
        print("NO")                        
    t -= 1
