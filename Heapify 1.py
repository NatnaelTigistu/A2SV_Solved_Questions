t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    visited = [False] * n
    possible = True
    
    for i in range(n):
        if not visited[i]:
            indices = []
            values = []
            
            j = i
            while j < n:
                visited[j] = True
                indices.append(j)
                values.append(a[j])
                j = 2 * j + 1   # because array is 0-indexed
            
            indices.sort()
            values.sort()
            
            for k in range(len(indices)):
                if values[k] != indices[k] + 1:
                    possible = False
                    break
        
        if not possible:
            break
    
    print("YES" if possible else "NO")
