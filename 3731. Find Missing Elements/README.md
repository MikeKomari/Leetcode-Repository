# 3731. Find Missing Elements

**Difficulty:** Easy

## Problem

Given an integer array `nums` consisting of unique integers, where the original array contained every integer within some range and the smallest and largest integers of that range are still present, return a sorted list of all the missing integers in the range. If no integers are missing, return an empty list.

## Approach

1. Convert `nums` to a set for O(1) membership checks
2. The smallest and largest values are guaranteed to be present, so only the range strictly between `min(nums)` and `max(nums)` can contain missing integers
3. Iterate that range in ascending order and collect every number not in the set

**Key Insight:** Because both bounds are guaranteed present, iterating from `min(nums) + 1` to `max(nums) - 1` in ascending order naturally produces a sorted result.

## Complexity

- **Time:** O(max - min) — O(n) since values are unique
- **Space:** O(n) for the set

## Solution

```python
class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        present = set(nums)
        return [x for x in range(min(nums) + 1, max(nums)) if x not in present]
```
