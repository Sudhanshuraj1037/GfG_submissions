# class Solution:
#     def getSecondLargest(self, arr):
#         # code here
#         n = len(arr)
#         largest = 0
#         secondLargest = arr[0]
#         for i in range(n):
#             if arr[i] > largest:
#                 largest = arr[i]
#             if largest > arr[i] > secondLargest:
#                 secondLargest = arr[i]
#         return secondLargest

class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        secondLargest = float('-inf')

        for x in arr:
            if x > largest:
                secondLargest = largest
                largest = x

            elif x > secondLargest and x != largest:
                secondLargest = x

        if secondLargest == float('-inf'):
            return -1

        return secondLargest