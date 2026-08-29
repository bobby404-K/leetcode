class Solution:
    def findDisappearedNumbers(self, nums):
        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]