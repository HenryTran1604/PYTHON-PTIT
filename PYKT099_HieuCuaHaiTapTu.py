set1, set2 = set(), set()

f =  open('DATA1.in')
while True:
    s = f.readline()
    if not s:
        break
    for x in s.split():
        set1.add(x.lower())

f = open('DATA2.in')
while True:
    s = f.readline()
    if not s:
        break
    for x in s.split():
        set2.add(x.lower())

for x in sorted(set1):
    if x not in set2:
        print(x, end = ' ')
print()
for x in sorted(set2):
    if x not in set1:
        print(x, end = ' ')

