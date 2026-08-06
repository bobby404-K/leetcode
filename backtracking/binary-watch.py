class Solution:
     def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hbits = [bin(h).count('1') for h in range(12)]
        mbits = [bin(m).count('1') for m in range(60)]

        result = []
        for h in range(12):
            need = turnedOn - hbits[h]
            if need < 0 or need > 6:
                continue
            hstr = str(h)
            for m in range(60):
                if mbits[m] == need:
                    result.append(hstr + ":" + (str(m) if m >= 10 else "0" + str(m)))
        return result