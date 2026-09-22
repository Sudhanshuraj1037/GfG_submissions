class Solution:
	def maxProduct(self,arr):
		# code here
		current_min = arr[0]
		current_max = arr[0]
		maximum = arr[0]
		
		for i in range(1, len(arr)):
		    if arr[i] < 0:
		        current_max, current_min = current_min, current_max
		    
		    current_max = max(current_max * arr[i], arr[i])
		    current_min = min(current_min * arr[i], arr[i])
            maximum = max(maximum, current_max)
	    return maximum