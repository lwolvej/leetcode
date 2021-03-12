class Solution:
    def numIslands(self, grid):
        x_len, y_len = len(grid), len(grid[0])
        book = [[False for _ in range(y_len)] for _ in range(x_len)]
        res = 0
        for i in range(x_len):
            for j in range(y_len):
                if (not book[i][j]) and (grid[i][j] == '1'):
                    self.bfs(grid, book, i, j, x_len, y_len)
                    res += 1
        return res

    def bfs(self, grid, book, now_x, now_y, x_max, y_max):
        queue = list()
        queue.append(Point(now_x, now_y))
        while queue:
            tmp_point = queue.pop()
            book[tmp_point.x][tmp_point.y] = True
            if tmp_point.x + 1 < x_max and grid[tmp_point.x + 1][tmp_point.y] == '1' and not book[tmp_point.x + 1][tmp_point.y]:
                queue.append(Point(tmp_point.x + 1, tmp_point.y))
            if tmp_point.y + 1 < y_max and grid[tmp_point.x][tmp_point.y + 1] == '1' and not book[tmp_point.x][tmp_point.y + 1]:
                queue.append(Point(tmp_point.x, tmp_point.y + 1))
            if tmp_point.x - 1 > -1 and grid[tmp_point.x - 1][tmp_point.y] == '1' and not book[tmp_point.x - 1][tmp_point.y]:
                queue.append(Point(tmp_point.x - 1, tmp_point.y))
            if tmp_point.y - 1 > -1 and grid[tmp_point.x][tmp_point.y - 1] == '1' and not book[tmp_point.x][tmp_point.y - 1]:
                queue.append(Point(tmp_point.x, tmp_point.y - 1)) 


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    a = 1
    if a == 1:
        print("YES")
    s = Solution()
    res = s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])
    print(res)
