class Solution:
    def generateParenthesis(self, n):
        self.res = []
        if n <= 0:
            return []
        self.dfs(0, 0, n, '')
        return self.res

    def dfs(self, l, r, n, cur):
        if r > l or l > n:
            return
        if l == n and l == r:
            self.res.append(cur)
        self.dfs(l + 1, r, n, cur + '(')
        self.dfs(l, r + 1, n, cur + ')')

    def generateParenthesis2(self, n):
        res = []

        def generate(l, r, cur):
            if r > l or l > n:
                return
            if l == n and l == r:
                res.append(cur)
            generate(l + 1, r, cur + '(')
            generate(l, r + 1, cur + ')')
        generate(0, 0, '')
        return res
