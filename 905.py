class Solution:
    def sortArrayByParity(self, A):
        tmp, k = [], 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[k] = A[i]
                k += 1
            else:
                tmp.append(A[i])
        for tmp_num in tmp:
            A[k] = tmp_num
            k += 1
        return A

    def sortArrayByParity2(self, A):
        q, o = [], []
        for a in A:
            if a % 2:
                q.append(a)
            else:
                o.append(a)
        return o + q
