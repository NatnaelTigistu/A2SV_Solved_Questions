n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
res = 0

days = 1
for i in range(len(a)):
    if a[i] >= days:
        res += 1
        days += 1

print(res)