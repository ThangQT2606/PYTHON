from math import *

def check1(s, index):
    for i in range(index):
        if int(s[i]) >= int(s[i+1]):
            return False
    return True

def check2(s, index):
    for i in range(index, len(s)-1):
        if int(s[i]) <= int(s[i+1]):
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        s = input()
        INT_m, index = -1e9, 0
        if len(s) > 2:
            for i in range(len(s)):
                if int(s[i]) >= INT_m:
                    INT_m = int(s[i])
                    index = i
            if check1(s, index) and check2(s, index):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')