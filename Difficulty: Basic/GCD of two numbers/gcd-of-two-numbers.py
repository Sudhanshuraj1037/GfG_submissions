class Solution:
    def gcd(self, a, b):
        # code here
        while b != 0:
            rem = a%b
            a = b
            b = rem
        return a