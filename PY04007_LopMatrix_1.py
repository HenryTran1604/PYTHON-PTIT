class Matran:
    def __init__(self, row, col, a):
        self.row = row
        self.col = col
        self.a = a
    def trans(self):
        at = [[0 for _ in range(self.row)] for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                at[j][i] = self.a[i][j]
        return Matran(self.col, self.row, at)

    def __mul__(self, o):
        res = [[0 for _ in range(o.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(o.col):
                for k in range(self.col):
                    res[i][j] += self.a[i][k] * o.a[k][j]
        return Matran(self.row, o.col, res)
    def __str__(self):
        res = ''
        for i in range(self.row):
            for j in range(self.col):
                res += str(self.a[i][j]) + ' '
            res += '\n'
        return res

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        a = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            a[i] = list(map(int, input().split()))
        mat = Matran(n, m, a)
        print(mat * mat.trans())

        t -= 1
