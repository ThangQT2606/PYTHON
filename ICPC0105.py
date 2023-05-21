from math import*

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while(cnt <= t):
        s = input()
        delim = 'abcdefghijklmnopqrstuvwxyz'
        for x in delim:
            s = s.replace(x, ' ')
        a = s.split()
        # print(len(a))
        q = len(a)
        for i in range(q):
            a[i] = int(a[i])
        print(max(a))
        cnt += 1
