# Problem 643
# Inefficient first try:
# Run   O(n * k)
# Space O(1) 
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -999

        for i in range(len(nums) - k + 1):
            avg = 0
            for j in range(i, i + k):
                avg += nums[j]
            
            avg /= k
            if avg > maxAvg: 
                maxAvg = avg
            
        return maxAvg
'''

# Run   O(k+n-k)
#     = O(n)
# Space O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        theSum = 0
        for i in range(k):
            theSum += nums[i]
        
        maxSum = theSum

        for i in range(1, len(nums) - k + 1):
            theSum -= nums[i - 1]
            theSum += nums[i + k - 1]

            if theSum > maxSum:
                maxSum = theSum
        
        return (maxSum / k)
