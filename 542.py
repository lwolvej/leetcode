class Solution:
    def updateMatrix(self, matrix):
        row, col = len(matrix), len(matrix[0])
        queue = list()
        for i in range(row):
            for j in range(col):
                if not matrix[i][j]:
                    queue.append((i, j))
                else:
                    matrix[i][j] = row + col
        while queue:
            now_i, now_j = queue.pop(0)
            for u, v in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r, c = now_i + u, now_j + v
                if r > -1 and r < row and c > -1 and c < col and matrix[r][c] > matrix[now_i][now_j] + 1:
                    matrix[r][c] = matrix[now_i][now_j] + 1
                    queue.append((r, c))
        return matrix
