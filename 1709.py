t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ops = []
    
    # Step 1: Fix vertical order
    for i in range(n):
        if a[i] > b[i]:
            ops.append((3, i + 1))
            a[i], b[i] = b[i], a[i]
    
    # Step 2: Bubble sort a
    for _ in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                ops.append((1, j + 1))
                a[j], a[j + 1] = a[j + 1], a[j]
    
    # Step 3: Bubble sort b
    for _ in range(n):
        for j in range(n - 1):
            if b[j] > b[j + 1]:
                ops.append((2, j + 1))
                b[j], b[j + 1] = b[j + 1], b[j]
    
    print(len(ops))
    for op in ops:
        print(op[0], op[1])