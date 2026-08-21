class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        pairs = 0
        
        for num in nums:
            pairs += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1
        
        return pairs    