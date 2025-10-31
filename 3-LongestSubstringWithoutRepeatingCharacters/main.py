class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        total = 0
        j = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                total = max(total, i - j + 1)
            else:
                while s[i] in seen:
                    seen.remove(s[j])
                    j += 1
                seen.add(s[i])
        
        return total

    
def main():
    solution = Solution()
    print("Solution: 3\nAnswer: ", solution.lengthOfLongestSubstring("abcabcbb"))
    print("Solution: 1\nAnswer: ", solution.lengthOfLongestSubstring("bbbbb"))
    print("Solution: 3\nAnswer: ", solution.lengthOfLongestSubstring("pwwkew"))
    print("Solution: 3\nAnswer: ", solution.lengthOfLongestSubstring("bwf"))
    print("Solution: 2\nAnswer: ", solution.lengthOfLongestSubstring("aab"))
    print("Solution: 3\nAnswer: ", solution.lengthOfLongestSubstring("dvdf"))

if __name__ == "__main__":
    main()