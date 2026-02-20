t = int(input()) 

for _ in range(t):
    m, s = map(int, input().split())  
    b = list(map(int, input().split()))  

    sum_b = sum(b)  
    total_sum = sum_b + s  

    n = 0
    while n * (n + 1) // 2 < total_sum:
        n += 1

    if n * (n + 1) // 2 == total_sum and max(b) <= n:
        print("YES")
    else:
        print("NO")
