
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: abs(x))

        ans = 0
        n = len(nums)

        for i in range(n):
            square = nums[i] * nums[i]

            if i < n // 2:
                ans -= square
            else:
                ans += square

        return ans


