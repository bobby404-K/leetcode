class Solution:
    def smallerNumbersThanCurrent(self, nums):
        a = sorted(nums)
        return [a.index(x) for x in nums]