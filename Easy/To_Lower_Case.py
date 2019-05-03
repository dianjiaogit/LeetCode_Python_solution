# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, str: str) -> str:
        for i in range (0, len(str)):
            asc = ord(str[i])
            if 65 <= asc <= 90:
                str = str[:i] + chr(asc + 32) + str[i + 1 :]
        return str