class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        k -= sum(max(0, d - left) for d in diff)
        diff = [min(d, left) for d in diff]

        for i in range(len(diff)):
            if k == 0:
                break
            if diff[i] == left and left > 0:
                diff[i] -= 1
                k -= 1

        return sum(d * d for d in diff)