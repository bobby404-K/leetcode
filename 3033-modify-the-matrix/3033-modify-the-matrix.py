class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        col_max = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        
        return [
            [col_max[j] if matrix[i][j] == -1 else matrix[i][j] for j in range(n)]
            for i in range(m)
        ]