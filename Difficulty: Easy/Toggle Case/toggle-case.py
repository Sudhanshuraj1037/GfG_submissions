class Solution:
    def toggleCase(self, s):
        # code here
        result = ""
        for ch in s:
            if 65 <= ord(ch) <= 90:
                result += chr(ord(ch) + 32)
            elif 97 <= ord(ch) <= 122:
                result += chr(ord(ch) - 32)
        return result