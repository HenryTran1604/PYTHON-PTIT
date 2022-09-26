from sys import stdin
if __name__ == '__main__':
    for line in stdin:
        sen = ''
        for x in line.split():
            if x[-1] == '?' or x[-1] == '!' or x[-1] == '.':
                sen += x[:-1]
                print(sen.strip().capitalize())
                sen = ''
            else:
                sen += x + ' '
        # if len(sen) and sen[-1] != '?' and sen[-1] != '.' and sen[-1] != '!':
        #     print(sen.strip().capitalize())
        