# class Solution:
#     def getDivisors(self, n):
#         # code here
#         for i in range(1, n+1):
#             if n % i == 0:
#                 print(i, end=" ")
                
# class Solution:
#     def getDivisors(self, n):
#         ans = []

#         for i in range(1, n + 1):
#             if n % i == 0:
#                 ans.append(i)

#         return ans

class Solution:
    def getDivisors(self, n):
        ans = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                ans.append(i)

                if i != n // i:
                    ans.append(n // i)

            i += 1

        ans.sort()
        return ans