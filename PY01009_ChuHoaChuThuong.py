if __name__ == "__main__":
    s = input()
    hoa = 0;
    thuong = 0
    for i in range(0, len(s)):
        if s[i].islower():
            thuong += 1
        else:
            hoa += 1
    if hoa > thuong:
        print(s.upper())
    else:
        print(s.lower())

