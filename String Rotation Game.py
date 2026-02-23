t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    blocks = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            blocks += 1
            
    if s[0] == s[-1]:
        print(blocks)
    elif len(s) == blocks:
        print(blocks)
    else:
        print(blocks + 1)