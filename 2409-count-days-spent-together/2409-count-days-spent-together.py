class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a, b = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        return max(0, (sum([31,28,31,30,31,30,31,31,30,31,30,31][:int(b[:2])-1]) + int(b[3:])) - (sum([31,28,31,30,31,30,31,31,30,31,30,31][:int(a[:2])-1]) + int(a[3:])) + 1)