class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        original = s.count('1')
        best = 0

       
        for idx in range(1, len(blocks) - 1):
            ch, length = blocks[idx]
            if ch == '1':
                prev_zero = blocks[idx - 1][1]
                next_zero = blocks[idx + 1][1]
                best = max(best, prev_zero + next_zero)

        return original + best