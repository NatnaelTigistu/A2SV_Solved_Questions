t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i

    left = pos[a[0]]
    right = pos[a[0]]

    ok = True

    for i in range(1, n):
        current = pos[a[i]]

        if current < left - 1 or current > right + 1:
            ok = False
            break

        if current < left:
            left = current
        if current > right:
            right = current

    if ok:
        print("YES")
    else:
        print("NO")
