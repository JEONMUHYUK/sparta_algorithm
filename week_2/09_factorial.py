# Factorial(N) = N * Factorial(N-1)
# ...
# Factorial(1) = 1

def factorial(n):
    if n == 1:
        return  1
    return n * factorial(n-1) #factorial(n-1)은 4로 되기 때문에 반복시킬시 5! 가 된다.


print(factorial(5))