# Problem 649
# Run   O(n)
# Space O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantQ = []
        direQ    = []

        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiantQ.append(i)
            else:
                direQ.append(i)

        while radiantQ and direQ:
            dire = direQ.pop(0)
            radiant = radiantQ.pop(0)

            if radiant < dire:
                radiantQ.append(radiant + n)
            else:
                direQ.append(dire + n)

        return 'Radiant' if radiantQ else 'Dire'