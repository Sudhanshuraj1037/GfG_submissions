class Solution:
    def printNos(self, n):
        # Code here
        if n == 0:
            return
        
        print(n, end=" ")
        # n -= 1
        self.printNos(n-1)