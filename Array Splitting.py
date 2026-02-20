n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
    print(0)
    exit()

total = a[-1] - a[0]

gaps = []
for i in range(1, n):
    gaps.append(a[i] - a[i-1])

gaps.sort(reverse=True)
print(total - sum(gaps[:k-1]))