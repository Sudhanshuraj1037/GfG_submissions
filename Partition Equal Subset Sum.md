## 01. Partition Equal Subset Sum

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1)

### Problem Description

**Task:** Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.Note: Each element must be in exactly one subset.Examples:Input: arr = [1, 5, 11, 5]

#### Examples

##### Example 1

- **Output:**
```text
true
```
- **Explanation:** The two parts are [1, 5, 5] and [11].

##### Example 2

- **Input:**
```text
arr = [1, 3, 5]
```
- **Output:**
```text
false
```
- **Explanation:** This array can never be partitioned into two such parts.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(sum(arr) * n)
- **Expected Auxiliary Space Complexity:** O(sum(arr))

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-06 23:39:31
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def equalPartition(self, arr):
        total = sum(arr)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
```

*Generated on: 11/6/2026, 11:39:56 PM*