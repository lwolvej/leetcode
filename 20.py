class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    return False
                tmp = stack.pop()
                if (c == ')' and tmp != '(') or (c == ']' and tmp != '[') or (c == '}' and tmp != '{'):
                    return False
        return not stack

    def isValid2(self, s):
        map_flag = {')': '(', '}': '{', ']': '['}
        stack = list()
        for c in s:
            if c in map_flag:
                if not stack or stack[-1] != map_flag[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack



if __name__ == '__main__':
    s = Solution()
    res = s.isValid('((')
    print(res)
