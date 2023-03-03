def fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    # memoization table to store results of subproblems
    memo = [0] * (n+1)
    # base cases
    memo[0] = 0
    memo[1] = 1
    # fill memoization table using results of subproblems
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    # return result of original problem
    return memo[n]

print(fibonacci(4))