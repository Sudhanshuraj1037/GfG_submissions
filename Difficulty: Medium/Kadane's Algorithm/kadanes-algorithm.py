"""T(n3), S(1)"""

# class Solution:
#     def maxSubarraySum(self, arr):
#         # Code here
#         n = len(arr)
#         maxi = float('-inf')
# 
#         for i in range(0, n):
#             for j in range(i, n):
# 
#                 total = 0
#                 for k in range(i, j+1):
#                     total += arr[k]
# 
#                 maxi = max(total, maxi)
#         return maxi


"""T(n2), S(1)"""

# class Solution:
#     def maxSubarraySum(self, arr):
        
#         maxi = float('-inf')
#         for i in range(len(arr)):
            
#             total = 0
#             for j in range(i, len(arr)):
#                 total += arr[j]
                
#             maxi = max(total, maxi)
#         return maxi


"""T(n1), S(1), Kadane's Algo"""

class Solution:
    def maxSubarraySum(self, arr):
        current = arr[0]
        maximum = arr[0]
        
        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            maximum = max(current, maximum)
        return maximum
        