def swap_case(s):
    rev = ""
    for c in s:
        if c.isalnum():
            if c.islower():
                rev += c.upper()
            else:
                rev += c.lower()
        else :
            rev += c
    return rev

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)