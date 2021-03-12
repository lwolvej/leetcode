class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        res = [[] for _ in range(numRows)]
        res[0].append(1)
        res[1].append(1)
        res[1].append(1)
        now = 2
        while now < numRows:
            res[now].append(1)
            for i in range (1, now):
                res[now].append(res[now - 1][i - 1] + res[now - 1][i])
            res[now].append(1)
            now += 1
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.generate(5)
    print(res)
