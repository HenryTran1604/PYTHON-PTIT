a = [0] * 10000
def generate():
    a[1], a[2] = 1, 0.5
    for i in range(3, 10000):
       a[i] = a[i - 2] + 1/i

if __name__ == '__main__':
    generate()
    t = int(input())
    while t > 0:
        n = int(input())
        print('%.6f' % a[n])
        t -= 1