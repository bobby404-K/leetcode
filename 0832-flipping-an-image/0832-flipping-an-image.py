class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        
        for row in image:
            left, right = 0, n - 1
            while left <= right:            
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        
        return image