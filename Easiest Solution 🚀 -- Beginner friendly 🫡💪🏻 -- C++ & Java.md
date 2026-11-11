## 01. Easiest Solution 🚀 || Beginner friendly 🫡💪🏻 || C++ & Java

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/search-for-subarray/1)

### Problem Description

**Task:** You are given two integer arrays a[] and b[]. Return all the starting indexes of all the occurences of b[] as a subarray in a[].

#### Examples

##### Example 1

- **Input:**
```text
a[] = [2, 4, 1, 0, 4, 1, 1], b[] = [4, 1]Output: [1, 4]Explanation: b[] occurs as a subarray in a[] from index 1 to 2 and from index 4 to 5.
```

##### Example 2

- **Input:**
```text
a[] = [2, 4, 1, 0, 0, 3], b[] = [0]Output: [3, 4]Explanation: b[] occurs as a subarray in a[] from index 3 to 3 and from index 4 to 4.
```

##### Example 3

- **Input:**
```text
a[] = [1, 3, 5, 3, 0], b[] = [1, 3, 0]Output: []Explanation: There is no subarray occurs as b[] in a[]
```

#### Constraints

- **1.** `1 ≤ a.size() ≤ 1061 ≤ b.size() ≤ a.size()0 ≤ b[i], a[i] ≤ 104`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n + m)
- **Expected Auxiliary Space Complexity:** O(m)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-11 23:58:58
- **Status:** Correct
- **Marks:** 8

```python
class Solution:
    def search(self, a, b):
        n, m = len(a), len(b)

        if m == 0:
            return list(range(n + 1))

        # Build LPS array
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and b[i] != b[j]:
                j = lps[j - 1]

            if b[i] == b[j]:
                j += 1

            lps[i] = j

        # KMP search
        result = []
        i = j = 0

        while i < n:
            if a[i] == b[j]:
                i += 1
                j += 1

                if j == m:
                    result.append(i - m)
                    j = lps[j - 1]
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return result
```

*Generated on: 11/11/2026, 11:59:26 PM*