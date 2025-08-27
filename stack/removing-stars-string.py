# Problem 2390
# Run   O(n)
# Space O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        # stupid naming because bored lol
        stackPancakes = []
        for letter in s:
            if letter is '*':
                stackPancakes.pop()
            else:
                stackPancakes.append(letter)
        return ''.join(stackPancakes)
