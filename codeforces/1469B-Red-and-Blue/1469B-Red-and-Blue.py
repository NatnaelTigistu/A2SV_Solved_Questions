# max prefix sum of r
    s = 0
    max_r = 0
    for x in r:
        s += x
        max_r = max(max_r, s)
    
    # max prefix sum of b
    s = 0
    max_b = 0
    for x in b:
        s += x
        max_b = max(max_b, s)
    
    print(max_r + max_b)