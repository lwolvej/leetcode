class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0: 
            return 0
        begin = 0
        end = 1
        max_len = 1
        now_len = 1
        while end < len(s):
            j = begin
            now_index = begin
            flag = False
            while j < end:
                if s[j] == s[end]:
                    flag = True
                    now_index = j
                    break;
                j += 1
            if flag:
                now_len = end - now_index
                begin = now_index + 1
            else:
                now_len += 1
            if now_len > max_len:
                max_len = now_len
            end += 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("pwwkew")
    print(res)