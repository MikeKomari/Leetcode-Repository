# 628. Maximum Product of Three Numbers

**Difficulty:** Easy

## Problem

Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

## Approach

1. Sort the array
2. The maximum product is either:
   - Product of the three largest numbers, OR
   - Product of the two smallest (potentially negative) numbers and the largest number
3. Return the maximum of these two possibilities

**Key Insight:** Two negative numbers multiplied together give a positive result, which could potentially create a larger product when combined with a large positive number.

## Complexity

- **Time:** O(n log n) due to sorting
- **Space:** O(1) or O(n) depending on sorting implementation

## Solution

```python
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1]
        )
```
