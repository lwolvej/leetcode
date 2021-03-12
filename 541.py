class Solution:
    def reverseStr(self, s, k):
        index, s_len, t = 0, len(s), list(s)
        while index < s_len:
            begin, end = index, index + k - 1
            if end >= s_len:
                end = s_len - 1
            while begin < end:
                t[begin], t[end] = t[end], t[begin]
                begin += 1
                end -= 1
            index += 2*k
        return ''.join(t)


