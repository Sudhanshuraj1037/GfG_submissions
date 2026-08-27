class Solution:
    def sequence(self, n: int) -> int:
        MOD = 10**9 + 7
    
        def product(count, num):
            if count == 0:
                return 1
    
            return (num * product(count - 1, num + 1)) % MOD
    
        def solve(term, num):
            if term > n:
                return 0
    
            current = product(term, num)
    
            return (current + solve(term + 1, num + term)) % MOD
    
        return solve(1, 1)