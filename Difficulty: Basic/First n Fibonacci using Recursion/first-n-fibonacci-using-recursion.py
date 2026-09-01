class Solution:
    def fibonacciNumbers(self, n: int) -> list[int]:
        result = []
    
        def fib(a, b, count):
            if count == 0:
                return
    
            result.append(a)
            fib(b, a + b, count - 1)
    
        fib(0, 1, n)
    
        return result