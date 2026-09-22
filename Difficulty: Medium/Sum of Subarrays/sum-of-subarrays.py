# class Solution:
#     def subarraySum(self, arr):
#         # code here 
#         total = 0
#         for i in range(0, len(arr)):
#             current = 0
#             for j in range(i, len(arr)):
#                 current +=arr[j]
#                 total = total + current
#         return total


class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total = 0

        for i in range(n):
            total += arr[i] * (i + 1) * (n - i)

        return total