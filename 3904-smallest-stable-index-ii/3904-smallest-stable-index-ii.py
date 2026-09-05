class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])

        max_so_far = nums[0]

        for i in range(n):
            max_so_far = max(max_so_far, nums[i])

            if max_so_far - suffix[i] <= k:
                return i

        return -1