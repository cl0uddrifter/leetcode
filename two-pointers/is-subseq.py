# Problem 392
# Run   O(n)
# Space O(1)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
            
        sPointer = 0
        for i in range(len(t)):
            if t[i] == s[sPointer]:
                sPointer += 1
            
            if sPointer >= len(s):
                return True
        
        return False
