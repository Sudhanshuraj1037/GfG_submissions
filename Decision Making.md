## 01. Decision Making

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/decision-making/1)

### Problem Description

**Task:** Given two integers, n and m. The task is to check the relation between n and m. Print "less" if n < m, "equal" if n = = m, and "greater" if n > m.Examples : Input: n = 4, m = 8

#### Examples

##### Example 1

- **Output:**
```text
greater
```
- **Explanation:** 8 > 4 so print 'greater'.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(1)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-31 22:51:27
- **Status:** Correct
- **Marks:** 1

```python
n = int(input())
m = int(input())

# code here
if n<m:
    print("less", end = '')
elif n == m:
    print("equal", end ='')
else:
    print("greater", end = '')
```

*Generated on: 10/31/2026, 11:02:37 PM*