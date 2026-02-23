n = int(input())

total_watched = sum(list(map(int, input().split())))

print((((n+1)*n) // 2) - total_watched)