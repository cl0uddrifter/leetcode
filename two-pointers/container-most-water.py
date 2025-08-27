# Problem 11
# Run   O(n)
# Space O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            x = r - l 
            if height[l] > height[r]:
                y = height[r]
            else:
                y = height[l]
            area = x * y
            if area > maxArea:
                maxArea = area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
