class Solution:
    def my_pow(self,x,n) -> float:
        if n == 0:
            return 1
        if n > 0:
            #Binary exponentiation
            #x ^ n = (x^2)^(n//2) for even n
            #x ^ n = x * (x^2)^(n//2) for odd n
            if n % 2 == 0:
                return self.my_pow(x * x, n // 2)
            else:
                return x * self.my_pow(x * x, (n-1) // 2)
        else:
            #For negative n, we return 1/(x^n)
            return 1 / self.my_pow(x, -n)
if __name__ == "__main__":
    obj = Solution()
    print(obj.my_pow(2.00000, 10))  # Output: 1024.00000
    print(obj.my_pow(2.10000, 3))   # Output: 9.26100
    print(obj.my_pow(2.00000, -2))  # Output: 0.25000
    print(obj.my_pow(0.00001, 2147483647))  # Output: 0.0
    print(obj.my_pow(1.00000, 2147483647))  # Output: 1.0