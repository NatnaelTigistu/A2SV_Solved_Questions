n = int(input())
for _ in range(n):
    ab = input()
    found = False
    for i in range(1,len(ab)):
        if ab[:i][0] == '0' or ab[i:][0] == '0':
            continue
        elif int(ab[:i]) < int(ab[i:]):
            print(ab[:i] +" "+ab[i:])
            found = True
            break
        else:
            continue
    if not found : print(-1)