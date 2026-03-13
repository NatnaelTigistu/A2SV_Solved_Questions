n, k = map(int, input().split())
a = list(map(int, input().split()))

count = {}
l = 0
best_l = 0
best_r = 0

for r in range(n):
    count[a[r]] = count.get(a[r], 0) + 1

    while len(count) > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            del count[a[l]]
        l += 1

    if r - l > best_r - best_l:
        best_l = l
        best_r = r

print(best_l + 1, best_r + 1)