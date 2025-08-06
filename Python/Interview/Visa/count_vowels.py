class Solution:
    def maxVowels(self, s:str) -> int: #O(N-K) = O(N) Sliding Window Approach; O(1) Space Complexity
        _vowels = set("aeiou")
        _vowels_count = 0
        _count = 0
        #l, r, k = 0, 0, 3
        k = 3  # Length of the substring to check for vowels
        n = len(s)

        for i in range(k):
            _vowels_count += int(s[i] in _vowels)

        _count += 1 if _vowels_count == 2 else 0 
        # Sliding window approach
        # We will slide the window of size k across the string and count the vowels in that window.
        # If the count of vowels in that window is 2, we increment our count
        # We will also update the count of vowels as we slide the window by removing the character
        # that is sliding out of the window and adding the character that is sliding into the window
        for i in range(k, n):
            _vowels_count += int(s[i] in _vowels)
            _vowels_count -= int(s[i - k] in _vowels)
            _count += 1 if _vowels_count == 2 else 0

        return _count


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

if __name__ == "__main__":
    s = "abciiidef"
    sol = Solution()
    print(sol.maxVowels(s))

#Time Complexity: O(N) where N is the length of the string and K is the length of the substring being checked for vowels.
