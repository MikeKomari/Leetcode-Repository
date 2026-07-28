# 3517. Smallest Palindromic Rearrangement I

**Difficulty:** Easy

## Problem

Given a string `s`, return the lexicographically smallest palindromic rearrangement of `s`.

## Approach

1. Count the frequency of each character using an array of size 26
2. For each character, put half its occurrences into the left half of the result
3. If a character has an odd count, exactly one goes into the middle
4. Return `left + middle + reversed(left)` to form the palindrome

## Complexity

- **Time:** O(n) where n is the length of s
- **Space:** O(n) for the result string

## Solution

```python
class Solution: 
    def smallestPalindrome(self, s: str) -> str:
        arr = [0] * 26

        for a in s:
            arr[ord(a) - ord("a")]+=1

        L = ""
        M = ""
        for i in range(26):
            if arr[i] > 0:
                if arr[i] % 2 == 0:
                    L += (arr[i] // 2) * chr(ord("a") + i)
                else:
                    L += (arr[i] // 2) * chr(ord("a") + i)
                    M += chr(ord("a") + i)
        if len(L):
            return L + M + L[::-1]
        else:
            return M
```
