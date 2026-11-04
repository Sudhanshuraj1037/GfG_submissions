## 01. Linear Probing in Hashing

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/linear-probing-in-hashing-1587115620/1)

### Problem Description

**Task:** Given an array arr[] of integers and a hash table of size m, insert the elements of the array into the hash table using linear probing to handle collisions. Colliding elements must be mapped to the position [(value+1) % m]. If there is no space left to insert a new element, simply discard that element.Examples:Input: arr[] = [3, 11, 10], m = 3

#### Examples

##### Example 1

- **Output:**
```text
[-1, -1, -1, -1, 4, 14, 24, 44, -1, -1]
```
- **Explanation:** 4 % 10 = 4, So insert 4 in hashtable[4],14 % 10 = 4, but hashtable[4] is already filled Since there is a collision, use a linear Probing to find the next available slot. Insert 14 into next available position which is hashtable[5]. Continue the process for remaining element.Input: arr[] = [5, 5, 5, 5, 5], m = 5 Output: [5, -1, -1, -1, -1]Explanation: 5 % 5 = 0, So insert 5 in hashtable[0],Next, 5 % 5 = 0, but hashtable[0] is already filled and since number is same, it is mapped to the same position in the hash table.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n * m)
- **Expected Auxiliary Space Complexity:** O(m)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-04 23:21:45
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def linearProbing(self, arr, m):
        hash_table = [-1] * m

        for num in arr:
            index = num % m

            for _ in range(m):
                if hash_table[index] == -1:
                    hash_table[index] = num
                    break

                if hash_table[index] == num:
                    break

                index = (index + 1) % m

        return hash_table
```

*Generated on: 11/4/2026, 11:22:03 PM*