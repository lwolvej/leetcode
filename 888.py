class Solution:
    def fairCandySwap(self, A, B):
        a_sum, b_sum = sum(A), sum(B)
        exchange = abs(a_sum - b_sum) // 2
        b_set = set(B)
        if a_sum > b_sum:
            for a in A:
                if (a - exchange) in b_set:
                    return [a, a - exchange]
        else:
            for a in A:
                if (a + exchange) in b_set:
                    return [a, a + exchange]
        return [0, 0]
