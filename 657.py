class Solution:
    def judgeCircle(self, moves):
        row, col = 0, 0
        for c in moves:
            if c == 'U':
                row += 1
            elif c == 'D':
                row -= 1
            elif c == 'R':
                col += 1
            elif c == 'L':
                col -= 1
        return row == 0 and col == 0

    def judgeCircle2(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

if __name__ == '__main__':
    _a_b = 1
    print(_a_b)
