t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = float('inf')

    patterns = [
        "aa",
        "aba", "aca",
        "abca", "acba",
        "abbacca", "accabba"
    ]

    for p in patterns:
        if p in s:
            ans = min(ans, len(p))

    print(ans if ans != float('inf') else -1)
