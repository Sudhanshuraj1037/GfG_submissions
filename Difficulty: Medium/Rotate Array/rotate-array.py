class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n  # 1. Badi d values ko handle karne ke liye (Fixes out-of-bound)

        temp = []

        # Pehle d elements ko temp mein daala
        for i in range(0, d):
            temp.append(arr[i])

        # Baaki bache elements ko aage shift kiya
        for i in range(d, n):
            arr[i - d] = arr[i]

        # 2. temp se elements ko wapas array ke end mein daala (Syntax & Logic Fix)
        k = 0
        for i in range(n - d, n):
            arr[i] = temp[k]
            k += 1

        return arr
