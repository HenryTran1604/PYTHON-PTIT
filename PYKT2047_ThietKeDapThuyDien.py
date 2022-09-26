from sys import stdin

def lastOver(a, x):
    l, r, res = 0, len(a) - 1, 0
    while l <= r:
        m = (l + r) // 2
        if a[m] < x:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res


if __name__ == '__main__':
    c = []
    for line in stdin:
        c += list(map(int, line.split()))
    t = c[0]
    idx = 1
    while t > 0:
        n = c[idx]
        pos = [0] + c[idx + 1 : idx + n + 1]
        idx += n
        wall = [0] + c[idx + 1 : idx + n + 1]
        idx += n + 1
        water = [0] * (n + 1)
        totalWall = [0] * (n + 1)
        # tinh luong nuoc
        st = list()
        for i in range(1, n + 1):
            totalWall[i] = totalWall[i- 1] + wall[i]
            while len(st) != 0 and wall[i] >= wall[st[-1]]:
                st.pop()
            if len(st) == 0:
                water[i] = pos[i] * wall[i] - totalWall[i - 1]
            else:
                id = st[-1]
                water[i] =  water[id] + (pos[i] - pos[id] - 1)*wall[i] - (totalWall[i - 1] - totalWall[id])
            st.append(i)
        q = c[idx]
        idx += 1
        while q > 0:
            x = c[idx]
            idx += 1
            print(lastOver(water, x))
            q -= 1
        t -= 1
