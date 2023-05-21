
# print(hh)
def swap(hh):
    for i in range(16):
        hh.append(2 ** i)
def co_so4(so_mu, s, hh):
    x = []
    for i in range(0, len(s), so_mu):
        x.append(s[i:i+so_mu])
    
    for i in range(len(x)):
        c = x[i]
        c = c[::-1]
        res = 0
        for j in range(0, len(c)):
            if c[j] == '1':
                res += hh[j]
        print(res, end = '')

def co_so8(so_mu, s, hh):
    x = []
    for i in range(0, len(s), so_mu):
        x.append(s[i:i+so_mu])
    for i in range(len(x)):
        c = x[i]
        c = c[::-1]
        res = 0
        for j in range(0, len(c)):
            if c[j] == '1':
                res += hh[j]
        print(res, end = '')

def co_so16(so_mu, s, hh):
    x = []
    for i in range(0, len(s), so_mu):
        x.append(s[i:i+so_mu])
    for i in range(len(x)):
        c = x[i]
        c = c[::-1]
        # print(c)
        res = 0
        for j in range(0, len(c)):
            if c[j] == '1':
                res += hh[j]
        if res == 10:
            print('A', end = '')
        elif res == 11:
            print('B', end = '')
        elif res == 12:
            print('C', end = '')
        elif res == 13:
            print('D', end = '')
        elif res == 14:
            print('E', end = '')
        elif res == 15:
            print('F', end = '')
        else:
            print(res, end = '')
        # print(res, end = '')
if __name__ == '__main__':
    t = int(input())
    hh = []
    swap(hh)
    while(t > 0):
        co_so = int(input())
        s = input()
        for i in range(1, 5):
            if 2**i == co_so:
                so_mu = i
                break
        if so_mu != 1:
            while len(s) % so_mu != 0:
                s = '0' + s
        if co_so == 2:
            print(s, end = '')
        elif co_so == 4:
            co_so4(so_mu, s, hh)
        elif co_so == 8:
            co_so8(so_mu, s, hh)
        else:
            co_so16(so_mu, s, hh)
        print()
        t -= 1
