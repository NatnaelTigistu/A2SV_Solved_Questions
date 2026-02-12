num = int(input())
word = input()

word.lower()
letters = "qwertyuiopasdfghjklzxcvbnm"
for l in letters:
    if l not in word:
        print("NO")
        return
print("YES")