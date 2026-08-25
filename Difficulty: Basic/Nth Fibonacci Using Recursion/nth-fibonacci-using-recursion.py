class Solution:
    def nthFibonacci(self, n):
        # Code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        # n = (n-1)+(n-2)
        return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)