class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store the characters in the current window
        left = 0  # Left pointer of the sliding window
        max_len = 0  # To store the maximum length of the substring

        for right in range(len(s)):
            # If character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the new character and update max_len
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

        