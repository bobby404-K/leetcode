class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max1 = max(max1, current_count)
            else:
                current_count = 0
        
        return max1