## 01. Euler Totient Function

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/euler-totient-function4604/1)

### Problem Description

**Task:** Find the Euler Totient Function (ETF) Φ(n) for an input n. ETF is the count of numbers in {1, 2, 3, …, n} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

#### Examples

##### Example 1

- **Input:**
```text
n = 11
```
- **Output:**
```text
10
```
- **Explanation:** From 1 to 11, 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10 are relatively prime to 11.

##### Example 2

- **Input:**
```text
n = 16
```
- **Output:**
```text
8
```
- **Explanation:** From 1 to 16, 1, 3, 5, 7, 9, 11, 13 and 15 are relatively prime to 16.

#### Constraints

- **1.** `1 ≤ n ≤10⁵`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(sqrt(n))
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-13 23:51:50
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def etf(self, n):
        result = n
        p = 2

        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p

                result -= result // p

            p += 1

        if n > 1:
            result -= result // n

        return result
```

*Generated on: 11/13/2026, 11:52:22 PM*