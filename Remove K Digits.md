## 01. Remove K Digits

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/remove-k-digits/1)

### Problem Description

**Task:** Given a non-negative integer s represented as a string and an integer k, remove exactly k digits from the string so that the resulting number is the smallest possible, while maintaining the relative order of the remaining digits.The resulting number must not contain any leading zeros. If the resulting number is an empty string after the removal, return "0".Examples:Input: s = "4325043", k = 3

#### Examples

##### Example 1

- **Output:**
```text
2043
```
- **Explanation:** Remove the three digits 4, 3, and 5 to form the new number "2043" which is smallest among all possible removal.

##### Example 2

- **Input:**
```text
s = "765028321", k = 5Output: 221
```
- **Explanation:** Remove the five digits 7, 6, 5, 8 and 3 to form the new number "0221". Since we are not supposed to keep leading 0s, we get "221".Constraints:1 ≤ k ≤ |s| ≤ 10⁶

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n + k)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-07 23:55:36
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def removeKdig(self, s, k):
        stack = []

        for digit in s:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # Remove remaining digits from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
```

*Generated on: 11/7/2026, 11:56:00 PM*