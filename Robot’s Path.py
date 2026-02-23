n , k = map(int, input().split())
max_obs = ['#'] * k
max_obs = ''.join(c for c in max_obs)
road = input()

if max_obs in road:
    print("NO")
else:
    print("YES")
