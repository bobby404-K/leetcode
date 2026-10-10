
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        freq = [0] * 100001

        for d in diff:
            freq[d] += 1

        for d in range(100000, 0, -1):
            if k <= 0:
                break

            take = min(freq[d], k)
            freq[d] -= take
            freq[d - 1] += take
            k -= take

        return sum(d * d * freq[d] for d in range(100001))
