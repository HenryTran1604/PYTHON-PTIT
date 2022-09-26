def HaNoiTower(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        return
    HaNoiTower(n - 1, a, c, b)
    HaNoiTower(1, a, b, c)
    HaNoiTower(n - 1, b, a, c)

if __name__ == '__main__':
    n = int(input())
    HaNoiTower(n, 'A', 'B', 'C')