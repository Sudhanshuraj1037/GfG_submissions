## 01. Team Leaders with At Least 4 Members

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/team-leaders-with-at-least-4-members/1)

### Problem Description

**Task:** Given a DataFrame employee containing information about employees and their team leaders, find the names of all team leaders who have at least 4 direct reports. An employee is considered a direct report of a team leader if the employee's leaderId is equal to that team leader's id.
Return a DataFrame containing the names of all such team leaders.
Pandas Schema:
id: Unique ID for each employee (Primary key).
name: Name of the employee.
department: The department where the employee works.
leaderId: ID of the employee's team leader (null if the employee has no leader).
Input table:
Output table:

#### Examples

##### Example 1

- **Explanation:** Sarah is the team leader of John, Jack, Emma, Olivia, James, Thomas, David, and Lily (8 direct reports). Therefore, Sarah is included in the result.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-11-09 23:00:28
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def teamLeaders(self, employee):
        reports = employee.groupby('leaderId').size()
        leader_ids = reports[reports >= 4].index

        result = employee[employee['id'].isin(leader_ids)][['name']]

        return result.reset_index(drop=True)
```

*Generated on: 11/9/2026, 11:00:59 PM*