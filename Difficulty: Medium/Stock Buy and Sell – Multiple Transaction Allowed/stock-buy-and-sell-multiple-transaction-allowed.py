class Solution:
    def maxProfit(self, prices):
        # code here
        n = len(arr)
        sell = 0
        for i in range(0, n-1):
            if arr[i] <= arr[i+1]:
                sell = sell+ (arr[i+1] - arr[i])
        return sell