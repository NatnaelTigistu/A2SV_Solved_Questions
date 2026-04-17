from collections import Counter

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))

    L = Counter(c[:l])
    R = Counter(c[l:])
    for color in list(L.keys()):
        m = min(L[color], R[color])
        L[color] -= m
        R[color] -= m
        l -= m
        r -= m
    if l < r:
        L, R = R, L
        l, r = r, l

    cost = 0
    diff = (l - r) // 2
    for color in L:
        pairs = L[color] // 2
        take = min(pairs, diff)
        cost += take
        L[color] -= take * 2
        diff -= take
    cost += diff

    remaining = sum(L.values()) + sum(R.values())
    cost += remaining // 2

    print(cost)