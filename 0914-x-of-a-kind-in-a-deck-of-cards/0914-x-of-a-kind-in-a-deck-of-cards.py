from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck)
        overall_gcd = reduce(gcd, counts.values())
        return overall_gcd > 1