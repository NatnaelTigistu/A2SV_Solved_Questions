t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    casino = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])


    maxCoins = k
    for i in range(n):
        if casino[i][0] <= maxCoins and casino[i][1] >= maxCoins:
            maxCoins = max(casino[i][2],maxCoins)
    print(maxCoins)
