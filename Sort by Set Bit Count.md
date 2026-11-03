## 01. Sort by Set Bit Count

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1)

### Problem Description

**Task:** Given an array arr[] of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements. Note: For integers having same number of set bits in their binary representation, sort according to their position in the original array i.e., a stable sort.Examples:Input: arr[] = [5, 2, 3, 9, 4, 6, 7, 15, 32]

#### Examples

##### Example 1

- **Output:**
```text
[3, 5, 6, 1, 2, 4]
```
- **Explanation:** The integers in their binary representation are:3 - 0011 5 - 0101 6 - 0110 1 - 0001 2 - 0010 4 - 0100 hence the non-increasing sorted order is: [3, 5, 6], [1, 2, 4]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-11-03 23:19:40
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def sortBySetBitCount(self, arr):
        arr.sort(key=lambda x: x.bit_count(), reverse=True)
        return arr
```

#### Solution 2 (Python)

- **Submitted:** 2026-11-03 23:19:22
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def sortBySetBitCount(self, arr):
        arr.sort(key=lambda x: x.bit_count(), reverse=True)
        return arr
```

*Generated on: 11/3/2026, 11:20:00 PM*