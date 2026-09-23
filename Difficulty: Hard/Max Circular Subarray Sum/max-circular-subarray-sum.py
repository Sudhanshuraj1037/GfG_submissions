class Solution:
    def maxCircularSum(self, arr):
        total = sum(arr)

        current_max = max_sum = arr[0]
        current_min = min_sum = arr[0]

        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            max_sum = max(max_sum, current_max)

            current_min = min(arr[i], current_min + arr[i])
            min_sum = min(min_sum, current_min)

        # All elements are negative
        if max_sum < 0:
            return max_sum

        # Normal vs circular
        return max(max_sum, total - min_sum)