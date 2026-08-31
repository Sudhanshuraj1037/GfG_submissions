class Solution:
    def getAlternates(self, arr):
        # Code Here
        result = []
        a = len(arr)
        for i in range(0,a):
            if i%2 == 0:
                result.append(arr[i])
        return result