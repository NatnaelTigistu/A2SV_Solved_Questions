t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    res = []
    r = 1
    l = 0
    inc = True if p[r] > p[l] else False
    while r < n:
        res.append(p[l])
        if inc:
            while r < n and p[r] > p[l]:
                r += 1
                l += 1
            inc = False
        else:
            while r < n and p[r] < p[l]:
                r += 1
                l += 1
            inc = True
    res.append(p[-1])
    print(len(res))
    print(" ".join(str(n) for n in res))