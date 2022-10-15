from datetime import datetime

class GameThu:
    def __init__(self, ma, hoTen, gioVao, gioRa):
        self.ma = ma
        self.hoTen = hoTen
        self.gioVao = datetime.strptime(gioVao, '%H:%M')
        self.gioRa = datetime.strptime(gioRa, '%H:%M')
    
    def thoiGianChoi(self):
        return int((self.gioRa - self.gioVao).total_seconds() // 60)
    
    def __str__(self):
        return f'{self.ma} {self.hoTen} {self.thoiGianChoi() // 60} gio {self.thoiGianChoi() % 60} phut'

if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        a.append(GameThu(input(), input(), input(), input()))
    a.sort(key = lambda x : -x.thoiGianChoi())
    for x in a:
        print(x)

       
