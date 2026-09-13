class Solution:
    def nonRepeatingChar(self,s):
        #code here
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        for ch in count:
            if count[ch] == 1:
                return ch
        return '$'