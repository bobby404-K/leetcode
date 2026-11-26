class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice = True

        while n >= stones:
            n -= stones
            alice = not alice
            stones -= 1

        return not alice
