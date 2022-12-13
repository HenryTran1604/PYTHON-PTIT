class Tram:
    def __init__(self, maTram, tenTram, luongMua, thoiGianMua):
        self.maTram = maTram
        self.tenTram = tenTram
        self.luongMua = luongMua
        self.thoiGianMua = thoiGianMua
    def __str__(self):
        return self.maTram + ' ' + self.tenTram + ' ' + '%.2f'%(self.luongMua/(self.thoiGianMua/60))

if __name__ == '__main__':
    d = dict()
    n, idx = int(input()), 1
    for _ in range(n):
        maTram = 'T%02d'%idx
        tenTram = input()
        batDau = input()
        ketThuc = input()
        thoiGianMua = (int(ketThuc[:2]) * 60 + int(ketThuc[3:]) - (int(batDau[:2]) * 60 + int(batDau[3:])))
        luongMua = float(input())
        if tenTram in d:
            d[tenTram].luongMua += luongMua
            d[tenTram].thoiGianMua += thoiGianMua
        else:
            d[tenTram] = Tram(maTram, tenTram, luongMua, thoiGianMua)
            idx += 1
    for x in d:
        print(d[x])
    
        