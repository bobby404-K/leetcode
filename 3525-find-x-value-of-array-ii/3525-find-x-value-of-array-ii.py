class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [[0] * k for _ in range(4 * n)]
        prod = [1] * (4 * n)

        def merge(a, b):
            res = [0] * k

            for r in range(k):
                res[r] = tree[a][r]

            for r in range(k):
                res[(prod[a] * r) % k] += tree[b][r]

            return res, (prod[a] * prod[b]) % k

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree[node][v] = 1
                prod[node] = v
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node], prod[node] = merge(node * 2, node * 2 + 1)

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = [0] * k
                v = value % k
                tree[node][v] = 1
                prod[node] = v
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node], prod[node] = merge(node * 2, node * 2 + 1)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node][:], prod[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left_cnt, left_prod = query(node * 2, l, mid, ql, qr)
            right_cnt, right_prod = query(node * 2 + 1, mid + 1, r, ql, qr)

            res = left_cnt[:]

            for r in range(k):
                res[(left_prod * r) % k] += right_cnt[r]

            return res, (left_prod * right_prod) % k

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            cnt, _ = query(1, 0, n - 1, start, n - 1)

            ans.append(cnt[x])

        return ans
        