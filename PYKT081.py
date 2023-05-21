for i in range(int(input())):
    s = input()
    n = s.split(".")

    try:
        a = 0
        for i in n:
            if ( int(i) > 255 or int(i) < 0):
                a = 1
                break
        if a == 0 and len(n) == 4:
            print("YES")
        else:
            print("NO")
            
    except:
        print("NO")