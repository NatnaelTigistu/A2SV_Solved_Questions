def count_good_segments(n, k, a):
    from collections import defaultdict
    
    freq = defaultdict(int)
    r = 0
    unique = 0
    ans = 0
    
    for l in range(n):
        while r < n:
            if freq[a[r]] == 0 and unique == k:
                break
            if freq[a[r]] == 0:
                unique += 1
            freq[a[r]] += 1
            r += 1
        
        ans += r - l
        
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            unique -= 1
    
    return ans


n, k = map(int, input().split())
a = list(map(int, input().split()))

print(count_good_segments(n, k, a))