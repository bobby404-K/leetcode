class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def mark_safe(r, c):
            if board[r][c] != 'O':
                return
            stack = [(r, c)]
            board[r][c] = '#'
            while stack:
                row, col = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                        board[nr][nc] = '#'
                        stack.append((nr, nc))

        for i in range(m):
            mark_safe(i, 0)
            mark_safe(i, n - 1)

        for j in range(n):
            mark_safe(0, j)
            mark_safe(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'