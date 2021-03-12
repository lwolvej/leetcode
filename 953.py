class Solution:
    def isAlienSorted(self, words, order):
        return words == sorted(words, key=lambda w: [{c: i for i, c in enumerate(order)}[x] for x in w])
