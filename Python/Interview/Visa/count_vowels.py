class Solution:
    # def maxVowels(self, s: str) -> int: #Code signal (O(N * K))
    #     vowels = ("a", "e", "i", "o", "u")
    #     def countVowels(s) -> int:
    #         _count = 0
    #         if len(s) >= 3:
    #             for char in s:
    #                 if char in vowels:
    #                     _count+=1
    #         return _count

    #     i,j = 0, 0
    #     n = len(s)
    #     count_str = 0

    #     while j <= (n+1):
    #         j = i + 3
    #         substr = s[i:j]
    #         if countVowels(substr) == 2:
    #             count_str+=1
    #         i += 1
    #     return count_str

    def maxVowels(self, s: str) -> int: #Code signal (O(N * K))

        vowels = set("aeiou")
        max_vowels = 0
        left = 0
        right = 0
        k = 3

        freq = {}

        while (right < k):
            if s[right] in vowels:
                freq[s[right]] = freq.get(s[right], 0) + 1
                max_vowels += 1
            right += 1

        while(right < len(s)):

            if s[right] in vowels:
                freq[s[right]] = freq.get(s[right], 0) + 1
                max_vowels += 1

            if s[left] in vowels:
                freq[s[left]] -= 1
                if freq[s[left]] <= 0:
                    del freq[s[left]]
                    max_vowels -= 1
            
            left += 1
            right += 1
        
        return max_vowels


if __name__ == "__main__":
    s = "abciiidef"
    sol = Solution()
    print(sol.maxVowels(s))

#Time Complexity: O(N) where N is the length of the string and K is the length of the substring being checked for vowels.
