# 3536. Maximum Product of Two Digits

**Difficulty:** Easy

## Problem

You are given a positive integer `n`. Return the **maximum** product of any two digits in `n`.

**Note:** You may use the **same** digit twice if it appears more than once in `n`.

## Approach

1. Convert the integer to a string to access individual digits
2. Sort the digits in ascending order
3. Multiply the two largest digits (last two elements after sorting)
4. Return the product

## Complexity

- **Time:** O(d log d) where d is the number of digits
- **Space:** O(d) for the sorted string

## Solution

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        s = sorted(str(n))
        return int(s[-1]) * int(s[-2])
```
