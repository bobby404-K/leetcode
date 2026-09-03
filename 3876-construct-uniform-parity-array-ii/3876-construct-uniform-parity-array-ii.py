class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m = min(nums1)
        return m % 2 == 1 or all(x % 2 == 0 for x in nums1)