from math import*
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a%b)
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if ucln(a[i], a[j]) == 1:
                print(a[i], a[j])