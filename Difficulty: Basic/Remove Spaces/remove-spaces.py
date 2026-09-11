class Solution:
    def removeSpaces(self, s):
        # code here
        ans = ""
        
        for ch in s:
            if ch != " ":
                ans = ans + ch
        return ans