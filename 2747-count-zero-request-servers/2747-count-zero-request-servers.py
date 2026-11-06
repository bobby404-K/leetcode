class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        queries = sorted((q, i) for i, q in enumerate(queries))

        freq = [0] * (n + 1)
        ans = [0] * len(queries)

        left = right = active = 0
        m = len(logs)

        for q, idx in queries:
            while right < m and logs[right][1] <= q:
                s = logs[right][0]
                if freq[s] == 0:
                    active += 1
                freq[s] += 1
                right += 1

            lower = q - x

            while left < right and logs[left][1] < lower:
                s = logs[left][0]
                freq[s] -= 1

                if freq[s] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
