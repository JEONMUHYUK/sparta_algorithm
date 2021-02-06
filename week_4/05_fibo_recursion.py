input = 20

#  Fibo(n) = Fibo(n-1) + Fibo(n-2)
#  Fibo(1) = Fibo(2) = 1

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)

print(fibo_recursion(input))  # 6765

#반복형태로 문제가 계속 파생된게 있다면 다이나믹 프로그래밍 사용 -> 다이나믹 프로그래밍 사용시 메모이제이션 사용!