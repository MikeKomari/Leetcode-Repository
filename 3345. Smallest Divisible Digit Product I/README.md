# 3345. Smallest Divisible Digit Product I

**Difficulty:** Easy

## Problem

Given two integers `n` and `t`, return the smallest number greater than or equal to `n` such that the product of its digits is divisible by `t`.

## Approach

1. Start from `n` and check each number up to 100
2. For each candidate, compute the product of its digits by extracting them one at a time with `% 10` and `// 10`
3. Return the first number whose digit product is divisible by `t`

**Key Insight:** The answer is always found before 100 because any number containing the digit 0 has a digit product of 0, which is divisible by any `t`. The final `return 0` is unreachable with the given constraints.

## Complexity

- **Time:** O(1) — at most 100 iterations, each computing the digit product of at most 3 digits
- **Space:** O(1)

## Solution

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n < 101:
            digits = n
            product = 1

            while digits > 0:
                product *= digits % 10
                digits //= 10

            if product % t == 0:
                return n

            n += 1

        return 0
```
