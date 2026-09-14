class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        result = ""
        for ch in s:
            if ch != c:
                result += ch
        return result