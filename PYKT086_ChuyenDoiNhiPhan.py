import math

def convert(a):
    n, b = 0, 1
    for i in range(len(a) - 1, -1, -1):
        n += int(a[i]) * b
        b *= 2
    if n < 10:
        return n
    return chr(65 + n%10)
f = open('DATA.in')
t = int(f.readline())
while t > 0:
    b = int(f.readline())
    b = int(math.log2(b))
    s = f.readline().strip()
    while len(s) % b != 0:
        s = '0' + s
    for i in range(0, len(s), b):
        print(convert(s[i:i+b]), end='')
    print()
    t -= 1
