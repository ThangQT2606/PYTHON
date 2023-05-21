from math import *

class thisinh:
    def __init__(self, name, date, d1, d2, d3):
        self.name = name
        self.date = date
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def tb(self):
        self.d1 = (self.d1 + self.d2 + self.d3)
    def xuat(self):
        print(self.name, self.date, self.d1)
    
if __name__ == '__main__':
    name = input()
    date = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    d = thisinh(name, date, d1, d2, d3)
    d.tb()
    d.xuat()
