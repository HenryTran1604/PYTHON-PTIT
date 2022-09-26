def check(n):
    for i in range(0, len(n)):
        if n[i] != '4' and n[i] != '7':
            return False
    return True;


t = int(input())
while t > 0:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1
