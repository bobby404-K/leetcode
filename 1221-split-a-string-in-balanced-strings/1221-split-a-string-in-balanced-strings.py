class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        
        for ch in s:
            balance += 1 if ch == 'R' else -1
            if balance == 0:
                count += 1
        
        return count