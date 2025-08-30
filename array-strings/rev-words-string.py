# Problem 151
# Run   O(n)
# Space O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word  = []

        length = len(s)
        for i in range(length):
            if word and s[i] == ' ':
                words.append(''.join(word))
                word = []
            elif s[i].isalpha() or s[i].isdigit():
                word.append(s[i])

                if i == length - 1:
                    words.append(''.join(word))
                    word = []
                    
        return ' '.join(words[::-1])
        
