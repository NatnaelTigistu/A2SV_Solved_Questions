t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ones = s.count('1')
    zeros = n - ones
    
    if ones % 2 == 0:
        indices = [i + 1 for i in range(n) if s[i] == '1']
        print(len(indices))
        if indices:
            print(*indices)
        else:
            print()
            
    elif zeros % 2 == 1:
        indices = [i + 1 for i in range(n) if s[i] == '0']
        print(len(indices))
        if indices:
            print(*indices)
        else:
            print()
            
    else:
        print(-1)