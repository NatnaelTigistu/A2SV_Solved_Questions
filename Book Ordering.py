n = int(input())

w , h = map(int, input().split())
prev_height = max(w,h)

for _ in range(n-1):
    w , h = map(int, input().split())

    if max(w,h) <= prev_height:
        prev_height = max(w,h)
    elif min(w,h) <= prev_height:
        prev_height = min(w,h)
    else:
        print("NO")
        exit()
print("YES")
