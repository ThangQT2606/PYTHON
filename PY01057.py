from math import*

def nto(n):
    if n < 2: 
        return False
    else:
        for i in range(2, isqrt(n)+1):
            if n%i == 0:
                return False
        return True
def solve(n):
    dem_chan, dem_le = 0, 0
    for i in range(len(n)):
        if (nto(i) and nto(int(n[i]))):
            dem_chan += 1
        if (nto(i) == False and nto(int(n[i])) == False):
            dem_le += 1
    if dem_chan + dem_le == len(n):
        return True
    else:
        return False
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = input()
        if(solve(n)):
            print('YES')
        else:
            print("NO")