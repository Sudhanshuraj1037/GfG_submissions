## 01. Array Subset

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1)

### Problem Description

**Task:** Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].Examples:Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]

#### Examples

##### Example 1

- **Output:**
```text
false
```
- **Explanation:** b[] is not a subset of a[]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n + m)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-02 23:58:44
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def isSubset(self, a, b):
        freq = {}

        for num in a:
            freq[num] = freq.get(num, 0) + 1

        for num in b:
            if freq.get(num, 0) == 0:
                return False
            freq[num] -= 1

        return True
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-02 23:56:08
- **Status:** Correct
- **Marks:** 1

```python
class Solution:
    def isSubset(self, a, b):
        freq = {}

        for num in a:
            freq[num] = freq.get(num, 0) + 1

        for num in b:
            if freq.get(num, 0) == 0:
                return False
            freq[num] -= 1

        return True
```

*Generated on: 11/2/2026, 11:59:17 PM*