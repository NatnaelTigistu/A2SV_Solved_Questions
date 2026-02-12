for i in range(1,6):
    row = input().strip()
    j = row.find('1')
    if j != -1:
        print(abs(3-i) + abs(2-j//2) )
        break