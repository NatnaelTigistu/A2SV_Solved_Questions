from collections import Counter

t = int(input())

for _ in range(t):
    n,l,r = map(int,input().split())
    pair = n//2
    price = abs(pair - l)
    socks = list(map(int, input().split()))
    l_socks = socks[:pair]
    r_socks = socks[pair:]
    l_count = Counter(l_socks)
    r_count = Counter(r_socks)
    for sock in l_count:
        if sock in r_count:
            match = l_count[sock] - r_count[sock]
            price += match if match > 0 else 0
        else:
            price += l_count[sock]
    print(price)