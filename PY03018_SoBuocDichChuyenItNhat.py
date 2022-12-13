from queue import Queue
from sys import stdin
def solve(a, n, m):
    queue = Queue()
    vis = dict()
    vis[(0, 0)] = 0
    queue.put((0, 0))
    while not queue.empty():
        t = queue.get()
        x, y = t[0], t[1]
        s = vis[(x, y)]
        if x == n - 1 and y == m - 1:
            return s
        if x + 1 < n:
            dx = abs(a[x + 1][y] - a[x][y])
            if x + dx < n and (x + dx, y) not in vis:
                if x + dx == n - 1 and y == m - 1:
                    return s + 1
                queue.put((x + dx, y))
                vis[(x + dx, y)] = s + 1
        if y + 1 < m:
            dy = abs(a[x][y + 1] - a[x][y])
            if y + dy < m and (x, y + dy) not in vis:
                if x == n - 1 and y + dy == m - 1:
                    return s + 1
                queue.put((x, y + dy))
                vis[(x,y + dy)] = s + 1
        if x + 1 < n and y + 1 < m:
            dxy = abs(a[x + 1][y + 1] - a[x][y])
            if x + dxy < n and y + dxy < m and (x + dxy, y + dxy) not in vis:
                if x + dxy == n - 1 and y + dxy == m - 1:
                    return s + 1
                queue.put((x + dxy, y + dxy))
                vis[(x + dxy,y + dxy)] = s + 1
    return -1

if __name__ == '__main__':
    t = int(stdin.readline())
    while t > 0:
        n, m = map(int, stdin.readline().split())
        a = []
        for i in range(n):
            a.append(list(map(int, stdin.readline().split())))
        print(solve(a, n, m))
        t -= 1
    