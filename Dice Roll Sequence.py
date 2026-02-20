t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prev_changed = False
    count = 0

    for i in range(n - 1):
        if a[i] == a[i+1] or (a[i] + a[i+1] == 7):
            if not prev_changed:
                count += 1
                prev_changed = True
            else:
                prev_changed = False
        else:
            prev_changed = False
    print(count)