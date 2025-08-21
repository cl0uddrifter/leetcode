# Problem 345
# Run   O(n)
# Space O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AaEeIiOoUu'
        sList = list(s)
        idxs = []
        vs   = []

        for i in range(len(s)):
            if s[i] in vowels:
                idxs.append(i)
                vs.append(s[i])

        vs = vs[::-1]
        
        for i in range(len(vs)):
            sList[idxs[i]] = vs[i]
        
        return ''.join(sList)
