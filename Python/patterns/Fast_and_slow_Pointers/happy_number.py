class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n>0:
                n, r = divmod(n, 10)
                total_sum+= r ** 2
            return total_sum
        seen = set()
        while n not in seen and n!=1:
            seen.add(n)
            n = get_next(n)
        return n == 1