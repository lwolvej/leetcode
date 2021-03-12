class Solution:
    def projectionArea(self, grid):
        x_max_sum, y_max_sum, num = 0, 0, 0
        x_len, y_len = len(grid), len(grid[0])
        for i in range(x_len):
            x_max = grid[i][0]
            for j in range(y_len):
                if grid[i][j] != 0:
                    num += 1
                x_max = max(x_max, grid[i][j])
            x_max_sum += x_max
        for j in range(y_len):
            y_max = grid[0][j]
            for i in range(x_len):
                y_max = max(grid[i][j], y_max)
            y_max_sum += y_max
        return x_max_sum + y_max_sum + num
