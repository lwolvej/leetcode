class Solution:
    def commonChars(self, A):
        res = []
        min_len_char = min(A, key=len)
        for c in min_len_char:
            if all(c in item for item in A):
                res.append(c)
                A = [i.replace(c, '', 1) for i in A]
        return res
