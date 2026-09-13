class Solution:
    def checkPangram(self,s):
        #code here
        s = s.lower()
        
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ch not in s:
                return False
        return True