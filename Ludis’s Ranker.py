n = int(input())
ratings = list(map(int,input().split()))


sorted_ratings = sorted(ratings,reverse=True)
position = {}

for i,rating in enumerate(sorted_ratings):
    if rating not in position:
        position[rating] = i+1

print(*(position[r] for r in ratings))
