class Solution:
    def countCharacters(self, words, chars):
        total = 0

        for word in words:
            temp = list(chars)
            good = True

            for c in word:
                if c in temp:
                    temp.remove(c)
                else:
                    good = False
                    break

            if good:
                total += len(word)

        return total
