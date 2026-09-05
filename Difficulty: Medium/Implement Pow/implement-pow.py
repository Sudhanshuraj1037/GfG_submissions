class Solution:
    def power(self, b: float, e: int) -> float:
    
        if e < 0:
            b = 1 / b
            e = -e
    
        answer = 1.0
    
        while e > 0:
            if e % 2 == 1:
                answer *= b
    
            b *= b
            e //= 2
    
        return answer