class Solution:
    def getMinMax(self, arr):
        # code here
        n = len(arr)
        min = arr[0]
        max = arr[0]
        for i in arr:
            if i < min:
                min = i
            if i > max:
                max = i
        return min,max