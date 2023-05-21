class Rectangle:
    def __init__(self,dai,rong,mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau
    def perimeter(self):
        return (self.dai+self.rong)*2
    def area(self):
        return self.dai*self.rong
    def color(self):
        return self.mau.lower().capitalize()
    def check(self):
        if self.dai <=0 or self.rong <= 0:
            return 0
        return 1
    def __str__(self):
        if self.check() == 1:
            return ('{} {} {}'.format(self.perimeter(), self.area(), self.color()))     
            # print(self.perimeter(),self.area(),self.color(),sep=" ")
        else:
            return ("INVALID")          

arr = input().split()
if(int(arr[0])>0 and int(arr[1])>0):
     r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
     print(r)
else:
 print("INVALID")
