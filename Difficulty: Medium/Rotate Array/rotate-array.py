# class Solution:
#     def rotateArr(self, arr, d):
#         # code here
#         for i in range(0, d-1):
            
class Solution:
    def rotateArr(self, arr, d):
        d = d % len(arr)
        arr[:] = arr[d:] + arr[:d]