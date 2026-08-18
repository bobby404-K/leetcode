class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat = [val for row in mat for val in row]
        
        return [flat[i * c:(i + 1) * c] for i in range(r)]