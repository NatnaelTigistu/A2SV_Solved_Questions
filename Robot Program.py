t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = 0
    first_hit = -1
    
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        if x + pref == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    ans = 1
    k -= first_hit
    
    pref = 0
    cycle_hit = -1
    
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        if pref == 0:
            cycle_hit = i + 1
            break
    
    if cycle_hit == -1:
        print(ans)
        continue
    
    ans += k // cycle_hit
    print(ans)
