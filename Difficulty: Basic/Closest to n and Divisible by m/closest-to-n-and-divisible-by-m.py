class Solution:
    def closestNumber(self, n, m):
        m = abs(m)
    
        a = (n // m) * m
        b = a + m
    
        if abs(n - a) < abs(n - b):
            return a
        elif abs(n - b) < abs(n - a):
            return b
        else:
            return max(a, b, key=abs)