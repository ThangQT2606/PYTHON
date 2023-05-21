from math import*

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        s = input()
        for i in range(1, len(s)):
            if('1' <= s[i] <= '9'):
                print(s[i-1]*int(s[i]), end = '')
        print()
