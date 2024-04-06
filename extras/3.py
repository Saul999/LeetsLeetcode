class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        mapped = {}
        max_substring = 0
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] not in mapped:
                mapped[s[r]] = r
                max_substring = max(max_substring, r - l + 1)
            else:
                l = max(mapped[s[r]] + 1, l)
                mapped[s[r]] = r
                max_substring = max(max_substring, r - l + 1)
            r += 1
        
        return max_substring
