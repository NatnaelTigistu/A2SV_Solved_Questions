n = int(input())

x = sorted([int(x) for x in input().split()])
if n%2 == 0:
    print (x[n//2 - 1])
else:
    print (x[n//2])