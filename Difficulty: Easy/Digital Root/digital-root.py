class Solution:
    def digitalRoot(self, n: int) -> int:
        if n < 10:
            return n

        digit_sum = 0

        while n > 0:
            digit_sum += n % 10
            n //= 10

        return self.digitalRoot(digit_sum)