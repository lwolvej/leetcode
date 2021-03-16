class Solution:
    def candy(self, ratings) -> int:
        ratings_len = len(ratings)
        res = [1] * ratings_len
        for i in range(1, ratings_len):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(ratings_len - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)
