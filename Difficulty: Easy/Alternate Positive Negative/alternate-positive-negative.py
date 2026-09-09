class Solution:
    def rearrange(self,arr):
        # code here
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        i = 0
        j = 0
        k = 0
        
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1
            
            arr[k] = neg[j]
            k += 1
            j += 1
            
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
            
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
            
        