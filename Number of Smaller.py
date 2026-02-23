n , m = map(int, input().split())
a = list(map(int , input().split()))
b = list(map(int , input().split()))

count = 0
i = 0
j = 0
res = []

while i < len(a):
    if a[i] >= b[j]:
        res.append(count)
        j += 1

    else:
        count += 1
        i += 1
    
res.extend([count] * (len(b) - len(res)))
print(*res)