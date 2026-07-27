# 1464. Maximum Product of Two Elements in an Array

**Difficulty:** Easy

## Problem

Given the array of integers `nums`, you will choose two different indices `i` and `j` of that array. Return the maximum value of `(nums[i]-1)*(nums[j]-1)`.

## Approach

1. Find the maximum value using `max(nums)`
2. Remove it from the list
3. Find the second maximum using `max(nums)` again
4. Return `(max1 - 1) * (max2 - 1)`

**Key Insight:** To maximize `(a-1) * (b-1)`, we need the two largest values. By finding and removing the maximum first, the next `max()` call gives us the second largest.

## Complexity

- **Time:** O(n) - two passes to find max values
- **Space:** O(1) - only two variables used

## Solution

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)

        return (max1-1)*(max2-1)
```
