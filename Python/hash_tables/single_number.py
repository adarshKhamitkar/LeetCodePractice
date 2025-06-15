class Solution:
    def singleNumber(self, nums: list) -> int:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i,0) + 1
            
        print(counter)

        for key in counter:
            if counter.get(key) == 1: return key
        return -1

def main():
    nums1 = [4,1,2,1,2]
    nums2 = [2,2,1]
    nums3 = [1]
    nums4 = [1,2,3,4,5,6,7,8,9,10]
    nums5 = [1,2,3,4,5,6,7,8,9,10,11]
    sol = Solution()
    print(sol.singleNumber(nums1))
    print(sol.singleNumber(nums2))
    print(sol.singleNumber(nums3))
    print(sol.singleNumber(nums4))
    print(sol.singleNumber(nums5))

if __name__ == "__main__":
    main()

# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: The solution uses a dictionary to count occurrences of each number.
# The first loop counts the occurrences, and the second loop finds the number that appears only once.
# This is efficient for the problem at hand, as it ensures that we only traverse the list a couple of times.
