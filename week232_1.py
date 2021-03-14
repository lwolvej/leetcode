class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if (not s1) or (not s2) or len(s1) != len(s2):
            return False
        ff, ss = -1, -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if ff == -1:
                    ff = i
                elif ss == -1:
                    ss = i
                else:
                    break
        s1 = list(s1)
        s1[ff], s1[ss] = s1[ss], s1[ff]
        return "".join(s1) == s2
