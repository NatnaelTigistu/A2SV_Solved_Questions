n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
s = 0
c = 0

for r in range(n):
    s += a[r]
    
    while s >= k:
        c += n - r
        s -= a[l]
        l += 1

print(c)