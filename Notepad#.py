t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    possible = False

    for i in range(n-2):
        if s[i:i+2] in s[i+2:]:
            possible = True
            break
    
    if possible:
        print("YES")
    else:
        print("NO")

