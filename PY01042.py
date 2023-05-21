from math import*

def check(n):
    for i in range(len(n)):
        if(n[i] != '0' and n[i] != '1' and n[i] != '2'):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    while cnt <= t:
        cnt += 1
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")