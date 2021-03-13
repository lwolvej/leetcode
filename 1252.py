class Solution:
    def oddCells(self, m, n, indices):
        tmp = [[0 for _ in range(n)] for _ in range(m)]
        for indice in indices:
            x, y = indice
            for i in range(m):
                tmp[i][y] += 1
            for i in range(n):
                tmp[x][i] += 1
        res = 0
        for tt in tmp:
            for t in tt:
                if t % 2 != 0:
                    res += 1
        return res
