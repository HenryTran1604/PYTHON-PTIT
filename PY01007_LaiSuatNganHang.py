import math

t = int(input())
while t > 0:
    line = input()
    tmp = line.split(" ")
    n = float(tmp[0])
    x = float(tmp[1])
    m = float(tmp[2])
    # (1 + x)^k = m
    cs = 1 + x / 100
    y = math.log(m/n, cs)
    print(math.ceil(y))
    t -= 1
