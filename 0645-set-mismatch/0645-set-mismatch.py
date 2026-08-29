class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        s = sum(nums) - n * (n + 1) // 2

        ss = sum(x * x for x in nums) - n * (n + 1) * (2 * n + 1) // 6

        missing = (ss // s - s) // 2
        duplicate = missing + s

        return [duplicate, missing]