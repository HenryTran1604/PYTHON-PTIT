from itertools import permutations

if __name__ == '__main__':
    tmp = input()
    s = list(tmp)
    perm = permutations(s)
    for x in list(perm):
        for j in x:
            print(j, end = '')
        print()