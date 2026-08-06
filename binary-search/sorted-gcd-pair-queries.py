class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        cnt = [0] * (M + 1)
        for x in nums: cnt[x] += 1
        ex = [0] * (M + 1)
        for d in range(1, M + 1):
            c = sum(cnt[d::d])
            ex[d] = c * (c - 1) // 2
        for d in range(M, 0, -1):
            for m in range(2 * d, M + 1, d):
                ex[d] -= ex[m]
        for d in range(1, M + 1):
            ex[d] += ex[d - 1]
        from bisect import bisect_right
        return [bisect_right(ex, q) for q in queries]