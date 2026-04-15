t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    white = s[:k].count('W')
    ans = white

    for i in range(k, n):
        if s[i] == 'W':
            white += 1
        if s[i - k] == 'W':
            white -= 1
        
        ans = min(ans, white)
    
    print(ans)