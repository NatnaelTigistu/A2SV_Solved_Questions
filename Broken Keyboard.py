t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)
    i = 0
    working = set()

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        length = j - i
        
        if length == 1 or length % 2 != 0:
            working.add(s[i])
        
        i = j

    print(''.join(sorted(working)))