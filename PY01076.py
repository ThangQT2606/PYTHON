import math


t = int(input())
while(t > 0):
    t -= 1
    a = input()
    b = input()
    c = math.gcd(int(a),int(b))
    print(c)