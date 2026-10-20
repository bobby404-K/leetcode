class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        positions = {}
        
        for index, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(index)
            
        min_dist = float('inf')
        
        for num, indices in positions.items():
            if len(indices) >= 3:
                for x in range(len(indices) - 2):
                    i = indices[x]
                    k = indices[x + 2]
                    
                    dist = 2 * (k - i)
                    if dist < min_dist:
                        min_dist = dist
                        
        if min_dist == float('inf'):
            return -1
        return min_dist