t = int(input())
while t > 0:
    n = input()
    ans = ''
    carry = 0;
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) >= 5:
            x = ord(n[i])
            x += 1
            ans += chr(x)
            carry = 1
        else:
            ans += '0'
            carry = 0;
    t -= 1
    if carry > 0:
        ans[0]
    print(ans)
