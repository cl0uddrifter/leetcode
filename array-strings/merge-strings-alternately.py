# Problem 1768
# Time  O(n+m)
# Space O(n+m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = []
        if len(word1) == len(word2):
            for i in range(len(word1)):
                finalString.append(word1[i] + word2[i])
        else:
            if len(word1) > len(word2):
                for i in range(len(word2)):
                    finalString.append(word1[i] + word2[i])
                finalString += word1[len(word2):]
            else:
                for i in range(len(word1)):
                    finalString.append(word1[i] + word2[i])
                finalString += word2[len(word1):]
        return ''.join(finalString)
