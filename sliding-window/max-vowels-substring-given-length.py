# Problem 1456
# Run   O(n)
# Space O(k)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        maxScore = -999

        substr = s[:k]
        score = len([char for char in substr if char in vowels])
        if score > maxScore:
            maxScore = score

        for i in range(k, len(s)):
            if s[i] in vowels:
                score += 1
            if s[i - k] in vowels:
                score -= 1
            if score > maxScore:
                maxScore = score
        
        return maxScore
        
