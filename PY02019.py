from math import*
def uc(a, b):
    if b == 0:
        return a
    else:
        return uc(b, a%b)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if uc(a[i], a[j]) == 1:
                print(a[i], a[j])