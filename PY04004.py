from math import *
class PhanSo:
    def __init__(self, tu1, mau1, tu2, mau2):
        self.tu1 = tu1
        self.mau1 = mau1
        self.tu2 = tu2
        self.mau2 = mau2
    def cong(self):
        self.tu1 = self.tu1 * self.mau2 + self.tu2 * self.mau1
        self.mau1 = self.mau1 * self.mau2
    def toi_gian(self):
        ucln = gcd(self.tu1, self.mau1)
        self.tu1 //= ucln
        self.mau1 //= ucln
    def __str__(self):
        return f'{self.tu1}/{self.mau1}'

if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    p = PhanSo(tu1, mau1, tu2, mau2)
    p.cong()
    p.toi_gian()
    print(p)