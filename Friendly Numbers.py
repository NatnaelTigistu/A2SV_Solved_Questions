def digit_sum(n):
    return sum(int(d) for d in str(n))
n = int(input())
for _ in range(n):
    x = int(input())
    count = 0
    for y in range(x+1 , x + 91):
        if y - digit_sum(y) == x:
            count += 1
    print(count)