class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, n = 0, len(s)
        seen = defaultdict(int)
        j = 0

        for i in range(n):
            seen[s[i]] += 1
            while len(seen) > 2:
                seen[s[j]] -= 1
                if seen[s[j]] == 0:
                    seen.pop(s[j])
                j += 1
            res = max(res, i - j + 1)
        return res