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
                    # split: (count-1)//2 goes to L (mirrored),
                    # exactly 1 stays in the middle
                    L += (arr[i] // 2) * chr(ord("a") + i)
                    M += chr(ord("a") + i)
        if len(L):
            return L + M + L[::-1]
        else:
            return M