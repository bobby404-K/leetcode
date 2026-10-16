class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right, val):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                length = end - start + 1
                tree_sq[node] = (
                    tree_sq[node]
                    + 2 * val * tree_sum[node]
                    + length * val * val
                ) % MOD

                tree_sum[node] = (
                    tree_sum[node] + length * val
                ) % MOD

                lazy[node] += val
                return

            mid = (start + end) // 2
            push(node, start, end, mid)

            update(node * 2, start, mid, left, right, val)
            update(node * 2 + 1, mid + 1, end, left, right, val)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        def push(node, start, end, mid):
            val = lazy[node]
            if val == 0 or start == end:
                return

            for child, l, r in (
                (node * 2, start, mid),
                (node * 2 + 1, mid + 1, end)
            ):
                length = r - l + 1

                tree_sq[child] = (
                    tree_sq[child]
                    + 2 * val * tree_sum[child]
                    + length * val * val
                ) % MOD

                tree_sum[child] = (
                    tree_sum[child] + length * val
                ) % MOD

                lazy[child] += val

            lazy[node] = 0

        last_seen = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)

            
            update(1, 0, n - 1, prev + 1, i, 1)

            ans = (ans + tree_sq[1]) % MOD
            last_seen[x] = i

        return ans