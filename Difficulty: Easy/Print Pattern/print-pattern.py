class Solution:
    def pattern(self, n):
    # Result list to store the sequence
        result = []

        def recurse(current):
        # Append on the way down
            result.append(current)

        # Base case: stop when number is 0 or negative
            if current <= 0:
                return

        # Recursive call
            recurse(current - 5)

        # Append on the way back up (unwinding the stack)
            result.append(current)

        recurse(n)
        return result
