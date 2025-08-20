# Problem 1207
# Run   O(n)
# Space O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occs = {}
        for n in arr:
            if n in occs:
                occs[n] += 1
            else:
                occs[n] = 1
        
        return(
            len(list(set(occs.values()))) 
            ==
            len(list(occs.values()))
        )
