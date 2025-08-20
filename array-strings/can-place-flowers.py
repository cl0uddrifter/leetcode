# Problem 605
# Run   O(n)
# Space O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spotsClaimed = 0
        i = 0
        while spotsClaimed < n and i < len(flowerbed):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    spotsClaimed += 1
                    i += 1
            i += 1
        
        return spotsClaimed >= n
