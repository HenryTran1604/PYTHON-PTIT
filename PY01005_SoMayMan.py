n = input()
cnt = 0
for i in range(0, len(n)):
    if n[i] == '4' or n[i] == '7':
        cnt += 1
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")