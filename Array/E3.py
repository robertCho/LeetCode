class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_index_map = {}  # To store the last index of each character
        max_length = 0
        left = 0  # Left boundary of the current substring

        for right in range(n):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1

            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        n = len(s)
        max_length = 0

        # Check all possible substrings
        for i in range(n):
            # Use set to track unique characters
            seen = set()
            current_length = 0

            # Try to extend substring starting at i
            for j in range(i, n): 
                # If character is already seen, break inner loop
                if s[j] in seen:
                    break

                # Add new character to set and update length
                seen.add(s[j])
                current_length += 1
                max_length = max(max_length, current_length)

        return max_length
    
    def lengthOfLongestSubstringBruteForce2(self, s: str) -> int:
        n = len(s)
        max_length = 1
        for i in range(n):
            set_char = set()
            set_char.add(s[i])
            for j in range(i + 1, n):
                if s[j] in set_char:
                    break
                else:
                    set_char.add(s[j])
                cur_length = len(set_char)
                max_length = max(max_length, cur_length)
        return max_length


Solution = Solution()
print(Solution.lengthOfLongestSubstringBruteForce("abcabcbb"))
