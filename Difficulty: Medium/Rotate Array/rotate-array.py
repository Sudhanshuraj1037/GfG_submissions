# class Solution:
#     def rotateArr(self, arr, d):
#         # code here
#         for i in range(0, d-1):

# class Solution:
#     def rotateArr(self, arr, d):
#         d = d % len(arr)
#         arr[:] = arr[d:] + arr[:d]

# class Solution:
#     def rotateArr(self, arr, d):
#         n = len(arr)
#         d = d % n

#         # Reverse first d elements
#         left, right = 0, d - 1
#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        # Reverse first d elements
        reverse(0, d - 1)

        # Reverse remaining elements
        reverse(d, n - 1)

        # Reverse the entire array
        reverse(0, n - 1)