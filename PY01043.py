def thuannghich(n):
    res = 0
    m = n
    dem = 0
    while n > 0:
        res = res*10 + n%10
        dem += 1
        n //= 10
    if m == res and dem % 2 == 0:
        return True
    else:
        return False

def cs(n):
    while n > 0:
        if (n%10)%2 != 0:
            return False
        n //= 10
    return True

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        n = int(input())
        if n >= 22:
            for i in range(22,n):
                if(cs(i) and thuannghich(i)):
                    print(i, end = ' ')
        print()
        cnt += 1