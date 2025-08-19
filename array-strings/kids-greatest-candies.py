# Problem 1431
# Run   O(n)
# Space O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for candy in candies:
            _candies = candy + extraCandies
            if _candies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
