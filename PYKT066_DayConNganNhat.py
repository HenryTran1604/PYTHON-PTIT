import math
from sys import *

if __name__ == '__main__':
    v = []
    for line in stdin:
        v += list(map(int, line.split()))
    t = v[0]
    pos = 1
    while t > 0:
        n, k = v[pos], v[pos + 1]
        pos += 2
        a = v[pos : pos + n]
        pos += n
        minLen = 10 ** 10
        for i in range(n):
            gcd = a[i]
            curLen = 0
            for j in range(i, n):
                gcd = math.gcd(gcd, a[j])
                if gcd == k:
                    curLen = j - i + 1
                    minLen = min(curLen, minLen)
                    break
        if minLen == 10 ** 10:
            print(-1)
        else:
            print(minLen)
        t -= 1