class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        a = [(x[0], x[1], x[2], i) for i, x in enumerate(intervals)]
        a.sort()

        starts = [x[0] for x in a]

        nxt = [0] * n

        for i in range(n):
            l, r = 0, n

            while l < r:
                m = (l + r) // 2

                if starts[m] > a[i][1]:
                    r = m
                else:
                    l = m + 1

            nxt[i] = l

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                skip = dp[k][i + 1]

                next_score, next_indices = dp[k - 1][nxt[i]]
                take = (
                    a[i][2] + next_score,
                    tuple(sorted((a[i][3],) + next_indices))
                )

                if take[0] > skip[0]:
                    dp[k][i] = take
                elif take[0] < skip[0]:
                    dp[k][i] = skip
                else:
                    if take[1] < skip[1]:
                        dp[k][i] = take
                    else:
                        dp[k][i] = skip

        return list(dp[4][0][1])