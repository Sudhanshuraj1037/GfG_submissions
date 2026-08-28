class Solution:
    def powerSet(self, s):
        result = []
    
        def solve(index, current):
            if index == len(s):
                result.append(current)
                return
    
            # Don't include s[index]
            solve(index + 1, current)
    
            # Include s[index]
            solve(index + 1, current + s[index])
    
        solve(0, "")
    
        return result