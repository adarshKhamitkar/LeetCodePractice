class Solution:
    def maxVowels(self, s: str) -> int: #Code signal (O(N * K))
        vowels = ("a", "e", "i", "o", "u")
        def countVowels(s) -> int:
            _count = 0
            if len(s) >= 3:
                for char in s:
                    if char in vowels:
                        _count+=1
            return _count

        i,j = 0, 0
        n = len(s)
        count_str = 0

        while j <= (n+1):
            j = i + 3
            substr = s[i:j]
            if countVowels(substr) == 2:
                count_str+=1
            i += 1
        return count_str

if __name__ == "__main__":
    s = "abciiidef"
    sol = Solution()
    print(sol.maxVowels(s))

#Time Complexity: O(N) where N is the length of the string and K is the length of the substring being checked for vowels.
