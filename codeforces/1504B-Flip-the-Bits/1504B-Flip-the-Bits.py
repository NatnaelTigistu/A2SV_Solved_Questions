t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))

    pref = [0]*n
    zeros = ones = 0

    for i in range(n):
        if a[i] == 0:
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            pref[i] = 1

    flip = 0
    possible = True

    for i in range(n-1, -1, -1):
        cur = a[i] ^ flip

        if cur != b[i]:
            if pref[i]:
                flip ^= 1
            else:
                possible = False
                break
    print("YES" if possible else "NO")