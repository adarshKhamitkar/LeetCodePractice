#Fibonacci

def fibIteration(n):
    if (n==0): return 0
    elif (n==1): return 1
    else:
        dp = [0] * (n+1)
        dp[0],dp[1] = 0,1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fibMemoization(n):
    memo = {}
    def fib(i):
        if i==0 : return 0
        if i==1 : return 1
        
        if i not in memo:
            memo[i] = fib(i-1)+fib(i-2)
        return memo[i]
    return fib(n)

print(fibIteration(9))
print(fibMemoization(9))

# Output
#34
#34
