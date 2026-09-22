class Solution:
    def majorityElement(self, arr):
        #code here
        count = {}
        n = len(arr)
        for nums in arr:
            if nums in count:
                count[nums] += 1
            else:
                count[nums] = 1
        
        for nums in count:
            if count[nums] > n // 2:
                return nums

        return -1
        