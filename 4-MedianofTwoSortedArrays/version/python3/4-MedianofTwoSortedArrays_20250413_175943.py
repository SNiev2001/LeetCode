# Last updated: 4/13/2025, 5:59:43 PM
'''
It checks for palindromes using a subfunction.
The subfunction uses two pointers , bounded within the array.
This function can be used for odd and even length palindromes
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal

            # Even length
            even_pal = expandAroundCenter(i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest
        
        return max(length)
            

        