n = int(input())
for _ in range(n):
    s = input().strip()
    t = input().strip()
    
    from collections import Counter
    
    cs = Counter(s)
    ct = Counter(t)
    
    possible = True
    for c in cs:
        if cs[c] > ct.get(c,0):
            possible = False
    if not possible:
        print("Impossible")
        continue

    extra = []
    for c in sorted(ct.keys()):
        extra.append([c] * (ct[c] - cs.get(c, 0)))
    
    result = []

    i = 0
    j = 0
    while i < len(s) and j < len(extra):
        if not extra[j]:
            j += 1
            continue
        if s[i] > extra[j][0]:
            result.extend(extra[j])
            j += 1
        else:
            result.append(s[i])
            i += 1
    for k in range(j, len(extra)):
        result.extend(extra[k])
    result.extend(s[i:])
    result = ''.join(char for char in result)
    print(result)

