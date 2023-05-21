while True:
    n = int(input())
    if n == 0: break
    else:
        a = []
        for i in range(n): a.append(int(input()))
        if(max(a) == min(a)): print("BANG NHAU")
        else: print(min(a), max(a))
