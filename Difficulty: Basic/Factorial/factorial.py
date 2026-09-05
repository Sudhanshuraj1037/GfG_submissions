class Solution:
    def factorial(self, n: int) -> int:
        # code here
        product = 1
        for i in range(1, n+1):
            product = i * product
        return product