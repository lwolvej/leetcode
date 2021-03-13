class Solution:
    def kWeakestRows(self, mat, k):
        mapping = {}
        for i, m in enumerate(mat):
            num = 0
            for mm in m:
                if mm == 1:
                    num += 1
                else:
                    break
            mapping[i] = num
        mapping = dict(sorted(mapping.items(), key=lambda e: e[1]))
        res = []
        for key in mapping.keys():
            res.append(key)
        return res[0::k]
