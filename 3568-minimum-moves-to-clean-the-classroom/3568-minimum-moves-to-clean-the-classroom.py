class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        sr = sc = 0
        litter = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        full = (1 << k) - 1

        queue = [[sr, sc, 0, energy]]
        front = 0

        visited = {}
        visited[(sr, sc, 0)] = energy

        steps = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while front < len(queue):
            size = len(queue) - front

            for _ in range(size):
                r, c, mask, rem = queue[front]
                front += 1

                if mask == full:
                    return steps

                if rem == 0 and classroom[r][c] != 'R':
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    new_rem = rem - 1

                    if new_rem < 0:
                        continue

                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        bit = litter[(nr, nc)]
                        new_mask |= (1 << bit)

                    if classroom[nr][nc] == 'R':
                        new_rem = energy

                    state = (nr, nc, new_mask)

                    if state in visited and visited[state] >= new_rem:
                        continue

                    visited[state] = new_rem
                    queue.append([nr, nc, new_mask, new_rem])

            steps += 1

        return -1