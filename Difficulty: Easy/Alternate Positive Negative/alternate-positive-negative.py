class Solution:
    def rearrange(self,arr):
        # code here
        # 1. Positive aur Negative numbers ko alag lists me store karein
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]

        i = 0  # pos list ka index tracker
        j = 0  # neg list ka index tracker
        k = 0  # Original arr ka index tracker

        # 2. Jab tak dono lists me elements hain, alternate karke arr me daalein
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1

            arr[k] = neg[j]
            k += 1
            j += 1

        # 3. Agar positive numbers bach gaye hain, toh unhe bache hue arr me copy karein
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1

        # 4. Agar negative numbers bach gaye hain, toh unhe bache hue arr me copy karein
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
