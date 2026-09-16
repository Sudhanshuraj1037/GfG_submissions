class Solution:
    def extractPoints(self, arr):
        n = len(arr)

        if n == 0:
            return []

        ans = [arr[0]]
        prev = 0

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                curr = 1
            elif arr[i] < arr[i - 1]:
                curr = -1
            else:
                continue

            if prev != 0 and curr != prev:
                ans.append(arr[i - 1])

            prev = curr

        if ans[-1] != arr[-1]:
            ans.append(arr[-1])

        return ans