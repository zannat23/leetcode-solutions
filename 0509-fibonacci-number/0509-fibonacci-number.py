class Solution(object):
    def fib(f , n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return f.fib(n - 1) + f.fib(n - 2)
        
n = 10
solution = Solution()
print(solution.fib(n))