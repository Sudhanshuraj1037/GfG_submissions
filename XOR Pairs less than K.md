## 01. XOR Pairs less than K

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/count-pairs-having-bitwise-xor-less-than-k/1)

### Problem Description

**Task:** Given an array arr[] and an integer k, we need to count the number of pairs from the given array such that the Bitwise XOR of each pair is less than k.

#### Examples

##### Example 1

- **Input:**
```text
arr = [1, 2, 3, 5], k = 5 Output: 4
```
- **Explanation:** Bitwise XOR of all possible pairs that satisfy the given conditions are:arr[0] ^ arr[1] = 1 ^ 2 = 3 arr[0] ^ arr[2] = 1 ^ 3 = 2 arr[0] ^ arr[3] = 1 ^ 5 = 4 arr[1] ^ arr[2] = 2 ^ 3 = 1 Therefore, the required output is 4.

##### Example 2

- **Input:**
```text
arr[] = [3, 5, 6, 8], k = 7 Output: 3Explnation: Bitwise XOR of all possible pairs that satisfy the given conditions are:arr[0] ^ arr[1] = 6arr[0] ^ arr[2] = 5arr[1] ^ arr[2] = 3Therefore, the required output is 3.
```

#### Constraints

- **1.** `1 ≤ arr.size(), k ≤ 5*10⁴¹ ≤ arr[i] ≤ 5*10⁴`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-08 23:22:08
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def cntPairs(self, arr, k):
        class TrieNode:
            def __init__(self):
                self.child = [None, None]
                self.count = 0

        root = TrieNode()
        ans = 0
        MAX_BIT = 16

        def insert(num):
            node = root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if node.child[bit] is None:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
                node.count += 1

        def count_less(num, limit):
            node = root
            count = 0

            for i in range(MAX_BIT, -1, -1):
                if node is None:
                    break

                a = (num >> i) & 1
                b = (limit >> i) & 1

                if b == 1:
                    if node.child[a] is not None:
                        count += node.child[a].count
                    node = node.child[1 - a]
                else:
                    node = node.child[a]

            return count

        for num in arr:
            ans += count_less(num, k)
            insert(num)

        return ans
```

*Generated on: 11/8/2026, 11:22:31 PM*