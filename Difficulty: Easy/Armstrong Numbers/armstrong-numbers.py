class Solution:
    def armstrongNumber (self, n):
        # code here 
        sum = 0
        original = n
        
        while n > 0:
            digit = n % 10
            sum = sum + digit ** 3
            n = n // 10
            
        return sum == original