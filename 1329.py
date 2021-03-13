class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        for k in range(-n+1, m-1):
            tmp = []
            for x in range(n):
                if -1 < x+k < m:
                    tmp.append(mat[x+k][x])
            tmp.sort(reverse=True)
            for x in range(n):
                if -1 < x+k < m:
                    mat[x+k][x] = tmp.pop()
        return mat
