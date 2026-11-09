import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        tree = [0] + [i & -i for i in range(1, k + 1)]

        def update(i, delta):
            i += 1
            while i <= k:
                tree[i] += delta
                i += i & -i

        def prefix(i):
            result = 0
            while i > 0:
                result += tree[i]
                i -= i & -i
            return result

        def kth(target):
            idx = 0
            bit = 1 << (k.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < target:
                    target -= tree[nxt]
                    idx = nxt
                bit >>= 1

            return idx

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k
            before = prefix(start)
            total = prefix(k)

            if total == 0:
                continue

            target = before + 1 if before < total else 1

            server = kth(target)

            update(server, -1)
            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
