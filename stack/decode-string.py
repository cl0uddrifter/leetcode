# Problem 394
# Run   O(n)
# Space O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentString = ""
        currentNumber = 0

        for char in s:
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)
            elif char == '[':
                currentState = (currentNumber, currentString)
                stack.append(currentState)

                currentString = ""
                currentNumber = 0
            elif char == ']':
                lastNumber, lastString = stack.pop()
                
                currentString = lastString + lastNumber * currentString
            else:
                currentString += char
        
        return currentString
