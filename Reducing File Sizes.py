n , m = map(int, input().split())

files = sorted(
    [[a, b, a - b] for _ in range(n) for a, b in [map(int, input().split())]],
    key=lambda x: x[2] , reverse= True
)

files_sum = sum(files[i][0] for i in range(n))

compressed_sum = sum(files[i][1] for i in range(n))

if compressed_sum >= m:
    print(-1)
    exit()

if files_sum <= m:
    print(0)
    exit()

compressed_size = 0
compressed_files = 0

required_compress_size = files_sum - m

i = 0
while required_compress_size > compressed_size:
    compressed_size += files[i][2]
    compressed_files += 1
    i += 1
print(compressed_files)