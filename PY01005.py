def cnt(n):
    dem4, dem7 = 0, 0
    while n > 0:
        m = n%10
        if(m == 4):
            dem4 += 1
        if(m == 7):
            dem7 += 1
        n //= 10
    if(dem4 + dem7 == 4 or dem4 + dem7 == 7):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    n = int(input())
    cnt(n)