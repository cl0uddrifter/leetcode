# Problem 1732
# Time  O(n)
# Space O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currentAlt = 0
        for alt in gain:
            currentAlt += alt
            if currentAlt > maxAlt:
                maxAlt = currentAlt
        return maxAlt
