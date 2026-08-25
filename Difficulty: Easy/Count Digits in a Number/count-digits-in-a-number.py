class Solution:
    def countDigits(self, n):
        # code here
            # Base case: if n becomes 0, no more digits to count
        if n == 0:
            return 0
            # Add 1 for the current digit and recurse with the remaining digits
        return 1 + self.countDigits(n // 10)
