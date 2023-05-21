
def object(x,y):
    return SP(x,y)
class SP:
    def __init__(self,thuc,ao) -> None:
        self.thuc = thuc
        self.ao = ao
    def nhan(self,SP):
        thuc = self.thuc*SP.thuc - self.ao*SP.ao
        ao = self.thuc*SP.ao + self.ao*SP.thuc
        return object(thuc,ao)
    def cong(self,PS):
        thuc = self.thuc + PS.thuc
        ao = self.ao + PS.ao
        return object(thuc,ao)
    def __str__(self) -> str:
        
        b = abs(self.ao)
        if self.ao > 0:
            return "{} + {}i".format(self.thuc,self.ao)
        else:
            return "{} - {}i".format(self.thuc,b)
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = [int(x) for x in input().split()]
        sp1 = SP(a[0],a[1])
        sp2 = SP(a[2],a[3])
        sp3 = sp1.cong(sp2)
        sp4 = sp3.nhan(sp1)
        sp5 = sp3.nhan(sp3)
        print(sp4, sp5, sep=', ',end='\n')
        