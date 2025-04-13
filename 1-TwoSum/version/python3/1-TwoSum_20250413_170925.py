# Last updated: 4/13/2025, 5:09:25 PM
'''
It need to use a sliding window.
It will grow while the right letter isn't new removing all letters unit
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

                