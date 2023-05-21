if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        s = input()
        n = int(input())
        n = str(n)
        dem = 0
        i = 0
        while i <= len(s) - len(n):
            a = s[i:(len(n)+i)]
            # print(a)
            if a == n:
                i += len(n)
                dem += 1
            else:
                i += 1
        print(dem)