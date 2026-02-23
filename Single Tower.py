n = int(input())

all_blocks = []
configuration = []

for _ in range(n):
    b = list(map(int, input().split()))
    configuration.append(b[1:])
    for i in range(1, len(b)):
        all_blocks.append(b[i])

sorted_blocks = sorted(all_blocks)

position = {value: idx for idx, value in enumerate(sorted_blocks)}

split = 0

for tower in configuration:
    for j in range(1, len(tower)):
       
        if position[tower[j]] != position[tower[j-1]] + 1:
            split += 1

combine = (n - 1) + split

print(split, combine)