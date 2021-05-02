def fastFib(n, memo):
#     global numCalls
#     numCalls += 1
#     print ('fib1 called with', n)
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]


def fib1(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)


# numCalls = 0
# n = 5
# res = fib1(n)
# print ('fib of', n,'=', res, 'numCalls = ', numCalls)