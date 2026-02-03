# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, c = (int(input()) for _ in range(3))

print(a**b)
print(pow(a,b,c))