class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, o):
        t = self.thuc + o.thuc
        a = self.ao + o.ao
        return SoPhuc(t, a)
    
    def __mul__(self, o):
        t = self.thuc*o.thuc - self.ao * o.ao
        a = self.thuc * o.ao + self.ao * o.thuc
        return SoPhuc(t, a)
    
    def __str__(self):
        return f'{self.thuc} + {self.ao}i'
    
test = int(input())
for _ in range(test):
    x, y, z, t = [int(x) for x in input().split()]
    a, b = SoPhuc(x, y), SoPhuc(z, t)
    c = (a + b) * a
    d = (a + b) * (a + b)
    print(c, d, sep = ', ')
