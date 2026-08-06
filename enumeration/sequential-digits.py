class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        L = len(str(low))
        H = len(str(high))
        result = []
        
        for i in range(L,  H+ 1):
            for j in range(0, len(digits) - i + 1):
                num = int(digits[j:j + i])
                if low <= num <= high:
                    result.append(num)
        
        return result 