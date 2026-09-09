# class Solution:
#     def reverseArray(self, arr):
#         # code here
#         n = len(arr)
#         for i in range(0,n):
#             if i < n:
#                 arr[i] = arr[n-1-i]
#             else:
                
#         return arr

class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        for i in range(0, n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return arr